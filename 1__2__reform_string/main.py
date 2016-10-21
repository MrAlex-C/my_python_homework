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
