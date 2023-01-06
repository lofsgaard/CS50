import requests
import sys
from sys import argv
import json

def main():
    if len(argv) == 2:
        try:
            user = float(argv[1])
            get_price(user)
        except:
            sys.exit('Command-line argument is not a number')
    elif len(argv) == 1:
        sys.exit('Missing command-line argument')
    else:
        sys.exit('Command-line argument is not a number')


def get_price(input):
    try:
        r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        if r.status_code == 200:
            dump = r.json()
            usd_value = dump['bpi']['USD']['rate_float']
            value = usd_value * float(input)
            print(f"${value:,.4f}")
        else:
            print("Something wrong")
            raise requests.RequestException
    except requests.RequestException:
        print("Something wrong")


if __name__ == "__main__":
    main()