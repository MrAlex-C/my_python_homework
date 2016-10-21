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
