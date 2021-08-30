import requests
import json


def lowercase(to_lower):
    to_lower = to_lower.lower()
    return to_lower



usd = 'http://www.floatrates.com/daily/usd.json'
eur = 'http://www.floatrates.com/daily/eur.json'
currency_cache = {}



#  taking necessary info to start searching
currency_to_exchange = lowercase(input())
target_currency = lowercase(input())
amount_to_exchange = float(input())

#  by default getting USD and EUR currency_rates and adding it to cache
usd_rates = requests.get(usd).json()
if currency_to_exchange == 'usd':
    pass
else:
    for b in usd_rates:
        if b == currency_to_exchange:
            f_rate = usd_rates[b]
            for c in f_rate:
                if c == 'inverseRate':
                    current_rate = f_rate[c]
                    currency_cache['usd'] = current_rate
eur_rates = requests.get(eur).json()
if currency_to_exchange == 'eur':
    currency_rates = eur_rates
else:
    for b in eur_rates:
        if b == currency_to_exchange:
            f_rate = eur_rates[b]
            for c in f_rate:
                if c == 'inverseRate':
                    current_rate = f_rate[c]
                    currency_cache['eur'] = current_rate
#  downloading current rates by getting json and adding to cache


url = 'http://www.floatrates.com/daily/' + currency_to_exchange + '.json'
currency_rates = requests.get(url).json()
print('Checking the cache...')
print('Oh it is in the cache!')
for x in currency_rates:
    if x == target_currency:
        f_rate = currency_rates[x]
        for y in f_rate:
            if y == 'rate':
                current_rate = f_rate[y]
                to_receive = amount_to_exchange * current_rate
                print('You received %.2f %s.' % (to_receive, target_currency.upper()))

def check_rates():

    while True:
        curr_to_check = lowercase(input())
        if len(curr_to_check) > 0 :
            to_check = float(input())
            print('Checking the cache...')
        for a in currency_cache:
                if a == curr_to_check:
                    print('Oh! It is in the cache!')
                    to_payout = currency_cache[curr_to_check] * to_check
                    print('You received %.2f %s.' % (to_payout, curr_to_check.upper()))
                else:
                    print('Sorry, but it is not in the cache!')
                    for b in currency_rates:
                        if b == curr_to_check:
                            f_rate = currency_rates[b]
                            for c in f_rate:
                                if c == 'rate':
                                    current_rate = f_rate[c]
                                    to_receive = to_check * current_rate
                                    print('You received %.2f %s.' % (to_receive, curr_to_check.upper()))
                                currency_cache[curr_to_check] = current_rate
                                check_rates()




check_rates()
'''
import requests
import json

code = input()
url = 'http://www.floatrates.com/daily/' + code + '.json'
rates = requests.get(url).json()
print(rates['usd'])
print(rates['eur'])
'''