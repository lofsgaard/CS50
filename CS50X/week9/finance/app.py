import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    userid = session["user_id"]
    shares = db.execute("SELECT symbol FROM purchases WHERE userid = ?", userid)
    db.execute("delete from stocks where userid = ?", userid)
    for share in shares:
        x = lookup(share["symbol"])
        db.execute("INSERT INTO stocks (symbol, price, userid) VALUES(?, ?, ?)", x["symbol"], x["price"], userid)
    purchases = db.execute("select distinct stocks.symbol, purchases.amount, stocks.price, (stocks.price * purchases.amount) as TotalValue from stocks  join purchases on purchases.symbol= stocks.symbol where purchases.userid = ? group by stocks.symbol", userid)

    total_value = db.execute(
        "select (stocks.price * purchases.amount) as Value from purchases join stocks on stocks.symbol = purchases.symbol where purchases.userid = ? group by purchases.symbol", userid)
    value = 0
    for x in total_value:
        value = value + x["Value"]
    balance = db.execute("SELECT cash FROM users WHERE id = ?", userid)
    for z in balance:
        total_balance = z["cash"]
    value_cash = float(value) + float(total_balance)
    return render_template("index.html", purchases=purchases, value_cash=value_cash, balance=balance)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    if request.method == "GET":
        return render_template("buy.html")
    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")
        stocks = lookup(symbol)
        if stocks is not None and shares.isdigit() and int(shares) > 0:
            userid = session["user_id"]
            balance = db.execute("SELECT cash FROM users WHERE id = ?", userid)
            for x in balance:
                cash = x["cash"]
            stock_price = float(stocks["price"])
            if int(cash) > float(stock_price) * int(shares):
                price = float(stock_price) * int(shares)
                owned = db.execute("SELECT * FROM purchases WHERE userid = ? and symbol like ?", userid, symbol.upper())
                print(owned)
                if owned:
                    db.execute("UPDATE purchases SET amount = amount + ? WHERE userid = ? and symbol = ?;",
                               shares, userid, symbol.upper())
                    db.execute("UPDATE users set cash=cash-? WHERE id = ?", price, userid)
                    db.execute("insert into history (userid, symbol, price, amount, user_action) VALUES(?,  ?,  ?,  ?, 'BUY')",
                               userid, symbol.upper(), stock_price, shares)

                else:
                    db.execute("INSERT INTO purchases (userid, symbol, amount) VALUES(?, ?, ?)", userid, symbol.upper(), shares)
                    db.execute("UPDATE users set cash=cash-? WHERE id = ?", price, userid)
                    db.execute("insert into history (userid, symbol, price, amount, user_action) VALUES(?,  ?,  ?,  ?, 'BUY')",
                               userid, symbol.upper(), stock_price, shares)
            else:
                return apology("You can not afford")

            return redirect("/")
        elif not shares.isdigit():
            return apology("Shares is not an int")
        elif stocks is None:
            return apology("Symbol does not exist, try again")
        else:
            return apology("Invalid share and stock")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    userid = session["user_id"]
    history = db.execute("select * from history where userid = ?", userid)
    return render_template("history.html", history=history)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "GET":
        return render_template("quote.html")
        symbol = request.form.get("symbol")
    if request.method == "POST":
        symbol = request.form.get("symbol")
        stocks = lookup(symbol)
        if stocks is not None:
            return render_template("quoted.html", stocks=stocks)
        else:
            return apology("Symbol does not exist, try again")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        pwhash = generate_password_hash(password)
        pwhash_confimation = generate_password_hash(confirmation)

        users = db.execute("select username from users")
        for user in users:
            if user["username"] == username:
                return apology("Username is taken")
        if username == '':
            return apology("Username is invalid")
        if password == '':
            return apology("Password is invalid")

        if password == confirmation:
            db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username, pwhash)
            return redirect("/login")
        else:
            return apology("Password is blank, or not the same")

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    userid = session["user_id"]
    stocks = db.execute("select symbol from stocks where userid = ?", userid)
    if request.method == "GET":
        return render_template("sell.html", stocks=stocks)
    else:
        sell_stock = request.form.get("symbol")
        shares = request.form.get("shares")
        stocks = lookup(sell_stock)
        owned = db.execute("SELECT * FROM purchases WHERE userid = ? and symbol like ?", userid, sell_stock.upper())
        balance = db.execute("SELECT cash FROM users WHERE id = ?", userid)
        stock_price = float(stocks["price"])
        price = float(stock_price) * int(shares)
        for z in owned:
            if z["amount"] >= int(shares):
                for x in balance:
                    cash = x["cash"]
                if owned:
                    db.execute("UPDATE purchases SET amount = amount - ? WHERE userid = ? and symbol = ?;",
                               shares, userid, sell_stock.upper())
                    db.execute("UPDATE users set cash=cash+? WHERE id = ?", price, userid)
                    db.execute("insert into history (userid, symbol, price, amount, user_action) VALUES(?,  ?,  ?,  ?, 'SELL')",
                               userid, sell_stock.upper(), stock_price, shares)
                updated_owned = db.execute("SELECT * FROM purchases WHERE userid = ? and symbol like ?", userid, sell_stock.upper())
                for y in updated_owned:
                    stock_owned = y["amount"]
                if stock_owned == 0:
                    db.execute("delete from purchases where userid like ? and symbol like ?", userid, sell_stock.upper())
                return redirect("/")
            else:
                return apology("You can't sell that many")


@app.route("/deposit", methods=["GET", "POST"])
@login_required
def deposit():
    userid = session["user_id"]
    if request.method == "GET":
        return render_template("deposit.html")
    if request.method == "POST":
        input_cash = request.form.get("cash")
        db.execute("update users set cash = cash + ? where id = ?", input_cash, userid)
        return redirect("/")