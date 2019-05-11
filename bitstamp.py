from exchange import Exchange
import requests

class Bitstamp(Exchange):
    def __init__(self):
        self.url = 'https://www.bitstamp.net/api/v2/ticker/btcusd/'
        self.sell_tax = 0.0025
        self.buy_tax = 0.0025
        self.last_buy_price = None
        self.last_sell_price = None

    def buy(self, amount, price):
        # actual code to buy on exchange goes here
        return amount * price

    def sell(self, amount, price):
        # actual code to sell on exchange goes here
        return amount * price

    def get_buy_price(self):
        try:
            r = requests.get(self.url)
            if r.status_code != 200:
                print('Could not fetch url: {} Status code: {}'.format(self.url, r.status_code))
                return None
            data = r.json()
            buy_price = float(data['ask'])
            self.last_buy_price = buy_price + self.buy_tax * buy_price
            return self.last_buy_price
        except Exception:
            return None

    def get_sell_price(self):
        try:
            r = requests.get(self.url)
            if r.status_code != 200:
                print('Could not fetch url: {} Status code: {}'.format(self.url, r.status_code))
                return None
            data = r.json()
            sell_price = float(data['bid'])
            self.last_sell_price = sell_price - self.sell_tax * sell_price
            return self.last_sell_price
        except Exception:
            return None