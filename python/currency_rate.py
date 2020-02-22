#!/usr/bin/env python3
#sudo pip3 install requests beautifulsoup4 lxml

import requests
from bs4 import BeautifulSoup

def get_html():
    url = 'http://cbr.ru/'
    r = requests.get(url)
    return r.text

def get_currency_rate(html, symbol):
    soup = BeautifulSoup(html, 'lxml')
    tag = soup.find('ins', text=f"{symbol}").find_parent('tr').find_all('td')[-1].text
    result = tag.replace('\xa0', '\n').split('\n')[-2]
    return result

def main():
    currency_list = ['Dollar_$', 'Euro_€', 'Gold_Au', 'Platinum_Pt']

    for currency in currency_list:
        curr_name = currency.split('_')[0]
        curr_symb = currency.split('_')[1]

        print(f"{curr_name} rate: {(get_currency_rate(get_html(), curr_symb))}")
    
if __name__ == '__main__':
    main()