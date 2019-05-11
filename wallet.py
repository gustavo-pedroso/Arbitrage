class Wallet:
    def __init__(self, name, exchange, balance_usd, balance_btc):
        self.name = name
        self.exchange = exchange
        self.balance_usd = balance_usd
        self.balance_btc = balance_btc

    def buy(self, amount, price):
        if self.balance_usd >= amount * price:
            self.exchange.buy(amount, price)
            self.balance_usd -= amount * price
            self.balance_btc += amount
        else:
            print('insufficient funds to buy btc on {}'.format(self.name))

    def sell(self, amount, price):
        if self.balance_btc >= amount:
            self.exchange.sell(amount, price)
            self.balance_btc -= amount
            self.balance_usd += amount * price
        else:
            print('insufficient funds to sell btc on {}'.format(self.name))

    def get_last_sell_price(self):
        return self.exchange.last_sell_price

    def get_last_buy_price(self):
        return self.exchange.last_buy_price

