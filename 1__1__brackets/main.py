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
