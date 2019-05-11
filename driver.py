from kraken import Kraken
from bittrex import Bittrex
from bitstamp import Bitstamp
from bitfinex import Bitfinex
from arbiter import Arbiter
from wallet import Wallet


kraken = Wallet(name='kraken', exchange=Kraken(), balance_usd=10000.0, balance_btc=1.0)
bittrex = Wallet(name='bittrex', exchange=Bittrex(), balance_usd=10000.0, balance_btc=1.0)
bitstamp = Wallet(name='bitstamp', exchange=Bitstamp(), balance_usd=10000.0, balance_btc=1.0)
bitfinex = Wallet(name='bitfinex', exchange=Bitfinex(), balance_usd=10000.0, balance_btc=1.0)


a = Arbiter(wallets=[kraken, bittrex, bitstamp], trade_amount=0.25, delay=20)
a.arbitrate()
