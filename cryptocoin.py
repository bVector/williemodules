import willie
import requests

@willie.module.commands('ticker')
def ticker(bot, trigger):
    prices = update_prices()
    bot.say('BTC: {}  LTC: {}  DOGE: {}'.format(prices['btc'], prices['ltc'], prices['doge']))


@willie.module.rule(r'\.([a-z42]{2,4})')
def cryptocoin(bot, trigger):
    prices = update_prices()
    if trigger.group(1) in prices:
        bot.say(trigger.group(1) + ':' +prices[trigger.group(1)])

def update_prices():
    prices = {}
    r = requests.get('http://altcoinfolio.com/cryptofolio/public/js/coins.json').json()
    for coin in r['coins']:
        prices[coin['sym']] = coin['price']
    return prices


