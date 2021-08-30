import requests

currency_cache = {}


def lowercase(to_lower):
    to_lower = to_lower.lower()
    return to_lower


def add_to_cache(curr_to_check, current_rate2):
    currency_cache[curr_to_check] = current_rate2


def check_currency_cache(curr_to_check, to_check):
    i = 0
    for a in currency_cache:
        if a == curr_to_check:
            print('Oh! It is in the cache!')
            to_payout = currency_cache[curr_to_check] * to_check
            print('You received %.2f %s.' % (to_payout, curr_to_check.upper()))
            i += 1
    if i == 0:
        print('Sorry, but it is not in the cache!')
        rate2 = to_cache(currency_rates, curr_to_check, to_check)
        return rate2


def to_cache(currency_rates3, curr_to_check, to_check):
    for g in currency_rates3:
        if g == curr_to_check:
            f_rate2 = currency_rates3[g]
            for h in f_rate2:
                if h == 'rate':
                    current_rate4 = f_rate2[h]
                    to_receive = to_check * current_rate4
                    print('You received %.2f %s.' % (to_receive, curr_to_check.upper()))
                    return current_rate4


usd = 'http://www.floatrates.com/daily/usd.json'
eur = 'http://www.floatrates.com/daily/eur.json'


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
rate = check_currency_cache(target_currency, amount_to_exchange)
add_to_cache(target_currency, rate)


def check_rates():

    while True:
        curr_to_check = lowercase(input())
        if len(curr_to_check) > 0:
            to_check = float(input())
            print('Checking the cache...')
            rate3 = check_currency_cache(curr_to_check, to_check)
            add_to_cache(curr_to_check, rate3)
        else:
            break


check_rates()
