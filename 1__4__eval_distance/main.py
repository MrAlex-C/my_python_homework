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
