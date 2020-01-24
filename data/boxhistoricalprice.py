from datetime import date
import requests
from bs4 import BeautifulSoup
from re import sub

todaysdate = date.today().strftime('%Y-%m-%d')

URL = 'https://coinmarketcap.com/currencies/bitcoin/markets/'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find('span', class_='cmc-details-panel-price__price')
for result in results:
    btc_price = result
    
URL = 'https://coinmarketcap.com/currencies/eos/markets/'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find('span', class_='cmc-details-panel-price__price')
for result in results:
    eos_price = result

URL = 'https://coinmarketcap.com/currencies/mixin/markets/'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find('span', class_='cmc-details-panel-price__price')
for result in results:
    xin_price = result
    
box_price = '${:,.2f}'.format((float(sub(r'[^\d.]', '', btc_price)) + float(sub(r'[^\d.]', '', eos_price)) * 1500 + float(sub(r'[^\d.]', '', xin_price)) * 8)/10000)

f = open("/Users/joker/github/xiaolai/regular-investing-in-box/data/box_price_history.txt", "a")
f.write(todaysdate + '\t' + btc_price + '\t' + eos_price + '\t' + xin_price  + '\t' + box_price +'\r')
f.close()

# on MacOSX, in terminal:
# > ctrontab -e
# 59 23 * * * python /Users/joker/github/xiaolai/regular-investing-in-box/data/boxhistoricalprice.py && cd /Users/joker/github/xiaolai/regular-investing-in-box/ && git pull && gaa && gcam 'historical price file auto-updated by python script' && gpuom
# > about ctron time setting, see: https://crontab.guru/#59_23_*_*_*