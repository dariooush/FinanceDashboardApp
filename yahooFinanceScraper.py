import requests
from bs4 import BeautifulSoup

URL = "https://finance.yahoo.com/cryptocurrencies/?offset=25&count=25"
webpage = requests.get(URL)
soup = BeautifulSoup(webpage.text, "html.parser")

tableRows = soup.find('table', class_='W(100%)').find('tbody').find_all('tr')

all_symbols = []
all_names = []
for row in tableRows:
    # rank += 1
    symbol = row.find('a', class_='Fw(600) C($linkColor)').text
    name = row.find('td', class_='Va(m) Ta(start) Px(10px) Fz(s)').text[0:-4]
    price = row.find('td', class_='Va(m) Ta(end) Pstart(20px) Fw(600) Fz(s)').text
    all_symbols.append(symbol)
    all_names.append(name)
    # print(symbol)

newDict = dict(zip(all_symbols, all_names))
print(newDict)