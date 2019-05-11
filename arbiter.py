import time

class Arbiter:
    def __init__(self, wallets, trade_amount, delay):
        self.wallets = wallets
        self.trade_amount = trade_amount
        self.delay = delay
        self.best_margin = 1000000000.0

    def arbitrate(self):
        while True:
            best_buy, best_sell = self.get_oportunities()

            if best_buy.exchange.last_buy_price < best_sell.exchange.last_sell_price: # buy from a sell on b
                if best_buy.balance_usd >= self.trade_amount * best_buy.exchange.last_buy_price:
                    if best_sell.balance_btc >= self.trade_amount:
                        best_buy.buy(self.trade_amount, best_buy.exchange.last_buy_price)
                        best_sell.sell(self.trade_amount, best_sell.exchange.last_sell_price)
                    else:
                        print('Not enough btc on {} to execute sell order'.format(best_sell.name))
                else:
                    print('Not enough usd on {} to execute buy order'.format(best_buy.name))
            else:
                print('No arbitrage margin found')

            print('best buy price: {} | best sell price: {}'
                  .format(best_buy.get_last_buy_price(), best_sell.get_last_sell_price()))

            if self.best_margin > best_buy.get_last_buy_price() - best_sell.get_last_sell_price():
                self.best_margin = best_buy.get_last_buy_price() - best_sell.get_last_sell_price()

            total_usd = sum([wallet.balance_usd for wallet in self.wallets])
            total_btc = sum([wallet.balance_btc for wallet in self.wallets])

            print('Money: {}, BTC: {}, Best Margin: {}'.format(total_usd, total_btc, self.best_margin))
            print('--------------------------------------------------------------------------------')
            time.sleep(self.delay)


    def get_oportunities(self):
        prices = []
        for wallet in self.wallets:
            wallet.exchange.get_buy_price()
            wallet.exchange.get_sell_price()
            prices.append(wallet)

        sell_prices = [(w.name, w.get_last_sell_price()) for w in prices]
        buy_prices = [(w.name, w.get_last_buy_price()) for w in prices]

        print('sell prices: {}'.format(sell_prices))
        print('buy prices: {}'.format(buy_prices))

        lowest_buy = sorted(prices, key=lambda x: x.get_last_buy_price())[0]
        highest_sell = sorted(prices, key=lambda x: x.get_last_sell_price())[-1]

        prices_no_lowest_buy = [wallet for wallet in prices if wallet != lowest_buy]
        prices_no_highest_sell = [wallet for wallet in prices if wallet != highest_sell]

        best_sell = sorted(prices_no_lowest_buy, key=lambda x: x.get_last_sell_price())[-1]
        best_buy = sorted(prices_no_highest_sell, key=lambda x: x.get_last_sell_price())[-1]

        margin1 = abs(lowest_buy.get_last_buy_price() - best_sell.get_last_sell_price())
        margin2 = abs(highest_sell.get_last_sell_price() - best_buy.get_last_buy_price())

        if margin1 > margin2:
            return lowest_buy, best_sell
        else:
            return best_buy, highest_sell
