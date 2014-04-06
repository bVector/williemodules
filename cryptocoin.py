import willie
import requests

@willie.module.commands('ticker')
def ticker(bot, trigger):
    prices = update_prices()
    bot.say('BTC: {}  LTC: {}  DOGE: {}'.format(prices['btc'], prices['ltc'], prices['doge']))


def update_prices():
    prices = {}
    r = requests.get('http://altcoinfolio.com/cryptofolio/public/js/coins.json').json()
    for coin in r['coins']:
        prices[coin['sym']] = coin['price']
    return prices


