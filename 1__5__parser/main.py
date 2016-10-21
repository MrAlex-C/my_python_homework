
#Ex5
codeValute = input("5) Введите код валюты\n")
codeValute = codeValute.upper()

import urllib
import urllib.request
from xml.etree import ElementTree

usdID = "R01235"
eurID = "R01239"
cnyID = "R01375"
uahID = "R01720"
jpyID = "R01820"

valute = ElementTree.parse(urllib.request.urlopen("http://www.cbr.ru/scripts/XML_daily.asp?date_req"))
for i in valute.findall('Valute'):
    valueID = i.get('ID')
    if valueID == usdID and codeValute == 'USD':
        rub = i.find('Value').text
        print("Курс доллара ", rub, " рублей")
    if valueID == eurID and codeValute == 'EUR':
        rub = i.find('Value').text
        print("Курс евро ", rub, " рублей")
    if valueID == cnyID and codeValute == 'CNY':
        rub = i.find('Value').text
        print("Курс юаней ", rub, " рублей")
    if valueID == uahID and codeValute == 'UAH':
        rub = i.find('Value').text
        print("Курс гривен ", rub, " рублей")
    if valueID == jpyID and codeValute == 'JPY':
        rub = i.find('Value').text
        print("Курс иен ", rub, " рублей")
