CREATE TABLE purchases (
	id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	dt datetime default current_timestamp,
	userid INTEGER NOT NULL,
	symbol TEXT NOT NULL,
	amount INTEGER NOT NULL
);


CREATE UNIQUE INDEX idx_purchases_id
ON purchases(id);

CREATE INDEX idx_purchases_username
ON purchases(username);



CREATE TABLE stocks (
	id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	userid INTEGER NOT NULL,
	symbol TEXT NOT NULL,
	price integer NOT NULL
);

CREATE TABLE history (
	id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	dt datetime default current_timestamp,
	userid INTEGER NOT NULL,
	symbol TEXT NOT NULL,
	price INTEGER NOT NULL,
	amount INTEGER NOT NULL,
	user_action TEXT NOT NULL
);