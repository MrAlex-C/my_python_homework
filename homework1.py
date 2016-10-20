# Ex1
def checkStr(str):
    counters = [0, 0, 0, 0, 0, 0]
    j = 0

    for i in str:
        j += 1
        if i == '(':
            counters[0] += 1
        elif i == ')':
            counters[1] += 1
        elif i == '[':
            counters[2] += 1
        elif i == ']':
            counters[3] += 1
        elif i == '{':
            counters[4] +=1
        elif i == '}':
            counters[5] +=1
        if i == ')' and counters[0] < counters[1]:
            return j
        if i == ']' and counters[2] < counters[3]:
            return j
        if i == '}' and counters[4] < counters[5]:
            return j
    if counters[0] == counters[1] \
            and counters[2] == counters[3] \
            and counters[4] == counters[5]:
        return "yes"
    else:
        return -1

str = input("1) Введите строку\n")
res = checkStr(str)
print(res)

# Ex2
#Через встроенные функции
#a
def lowerStr(string):
    """Переводит все слова в нижний регистр, кроме первой буквы первого слова"""
    string = string.lower()
    string = string.capitalize()

    return string

#б
# def

#в
def deleteEmail(string):
    #Удаляет email
    copyString = string
    counter = list(copyString).count('@')
    i = 0

    while i < counter:
        pos = copyString.find('@', 0, len(copyString)) #Позиция @
        if pos != 0 and pos != len(copyString) and pos != -1:
            if copyString[pos - 1].isalpha() and copyString[pos + 1].isalpha():
                dotPos = copyString.find('.', pos, copyString.find(' ', pos, len(copyString) - pos))
                if dotPos != -1 and dotPos != len(copyString):
                    if copyString[dotPos + 1].isalpha():
                        secondPos = copyString.find(' ', dotPos, len(copyString) - dotPos)
                        if secondPos == -1: secondPos = len(copyString)
                        firstPos = copyString.rfind(' ', 0, pos)
                        if firstPos == -1: firstPos = 0
                        copyString = copyString.replace(copyString[firstPos:secondPos], '[контакты запрещены]')
        i += 1

    return copyString

#г
def deleteBigNum(string):
    """Удаляет слова длинной более трех символов, состоящие только из цифр"""
    string = string.split(' ')
    copyString = string [:]
    for i in string:
        if i.isdigit() and len(i) > 3:
            copyString.remove(i)

    return ' '.join(copyString)

#С помощью регулярных выражений
import re
#а
def lowStr(string):
    string = string.lower()
    string = re.sub(r'^\w', string[:1].upper(), string)
    return string

#б
def delLink(string):
    # string = re.sub(, '[ссылки запрещены]', string)
    return string

#в
def delEmail(string):
    string = re.sub('\w+@\w+\.\w+','[контакты запрещены]', string)
    return string

#г
def delBigNum(string):
    length = len(string)
    string = re.sub('\d\d\d\d+', '', string)
    return string

str = input("2.1) Введите строку\n")
# Через функции строк
newStr = lowerStr(str)
newStr = deleteEmail(newStr)
newStr = deleteBigNum(newStr)
print(newStr)

str = input("2.2) Введите строку\n")
# Через регулярные выражения
newStr = lowStr(str)
newStr = delEmail(newStr)
newStr = delBigNum(newStr)
print(newStr)

# Ex3
def calcFromStr(string):
    listSum = re.findall('\d+\+\d+', string)
    listMultiply = re.findall('\d+\*\d+', string)
    listSub = re.findall('\d+\-\d+', string)
    listDiv = re.findall('\d+\/\d+', string)
    listAll = listSum + listMultiply + listSub + listDiv

    i = 0
    while i < len(listSum):
        operands = re.split('\+', listSum[i])
        listSum[i] = float(operands[0]) + float(operands[1])
        i += 1

    i = 0

    while i < len(listMultiply):
        operands = re.split('\*', listMultiply[i])
        listMultiply[i] = float(operands[0]) * float(operands[1])
        i += 1

    i = 0

    while i < len(listSub):
        operands = re.split('\-', listSub[i])
        listSub[i] = float(operands[0]) - float(operands[1])
        i += 1

    i = 0

    while i < len(listDiv):
        operands = re.split('\/', listDiv[i])
        listDiv[i] = float(operands[0]) / float(operands[1])
        i += 1

    i = 0

    while i < len(listAll):
        listAll[i] = listAll[i] + ' = '
        i += 1

    i = 0
    j = 0

    while i < len(listSum) :
        str = []
        str.append(listAll[j])
        str.append(listSum[i])
        print(str)
        i += 1
        j += 1

    i = 0

    while i < len(listMultiply):
        str = []
        str.append(listAll[j])
        str.append(listMultiply[i])
        print(str)
        i += 1
        j += 1

    i = 0

    while i < len(listSub):
        str = []
        str.append(listAll[j])
        str.append(listSub[i])
        print(str)
        i += 1
        j += 1

    i = 0

    while i < len(listDiv):
        str = []
        str.append(listAll[j])
        str.append(listDiv[i])
        print(str)
        i += 1
        j += 1

    return True

str = input("3) Введите строку\n")
calcFromStr(str)

#Ex4
def min(lst, max):
    """Возвращает минимально расстояние между различными элементам"""
    min = max
    i = 0
    while i < len(lst):
        j = 0
        l1 = re.split(' ', lst[i])
        while j < len(lst):
            if i != j:
                l2 = re.split(' ', lst[j])
                x1 = l1[0]
                y1 = l1[1]
                x2 = l2[0]
                y2 = l2[1]
                if mod(x1,y1, x2, y2) < min:
                    min = mod(x1, y1, x2, y2)
            j +=1
        i += 1
    return min

def max(lst):
    """Возвращает максимальное расстояние между различными элементами"""
    i = 0
    max = 0
    while i < len(lst):
        j = 0
        l1 = re.split(' ', lst[i])
        while j < len(lst):
            l2 = re.split(' ', lst[j])
            x1 = l1[0]
            y1 = l1[1]
            x2 = l2[0]
            y2 = l2[1]
            if mod(x1, y1, x2, y2) > max:
                max = mod(x1, y1, x2, y2)
            j += 1
        i += 1
    return max

def mod(X1, Y1, X2, Y2):
    res = [int(X1) - int(X2), int(Y1) - int(Y2)]

    return (res[0]**2 + res[1]**2)**(0.5)

#Читаем файл
file = open('C:\\Python35\\data for ex4')
myList = []

for line in file:
    myList.append(line.strip())
print("4) ")
print("max = ", max(myList))
print("min = ", min(myList,max(myList)))

file.close()

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