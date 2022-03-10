import random
import timeit

def generateArray(m = 50, n = 50, min_limit = 250, max_limit = 1011):
    matrix = [[random.randint(min_limit, max_limit) for i in range(m)] for i in range(n)]
    for i in range(m):
        for j in range(n):
         print(matrix[j][i], end = ' ')
        print()
    return matrix

def selectionSort(b):
    a = b.copy()
    for k in range(len(a)):
        for i in range(len(a[k]) - 1):
            m = i
            j = i + 1
            while j < len(a[k]):
                if a[k][j] < a[k][m]:
                    m = j
                j = j + 1
            a[k][i], a[k][m] = a[k][m], a[k][i]
    return a

def insertionSort(b):
    a = b.copy()
    for p in range(len(a)):
        for i in range(1, len(a[p])):
            k = a[p][i]
            j = i-1
            while j >= 0 and k < a[p][j]:
                a[p][j+1] = a[p][j]
                j -= 1
            a[p][j+1] = k
    return a

def exchangeSort(b):
    a = b.copy()
    for p in range(len(a)):
        for i in range(len(a[p])):
            for j in range(len(a[p]) - i - 1):
                if a[p][j] > a[p][j + 1]:
                    a[p][j], a[p][j + 1] = a[p][j + 1], a[p][j]
    return a

def shellsSort(b):
    a = b.copy()
    for p in range(len(a)):
        d = len(a) // 2
        while d:
            for i, el in enumerate(a[p]):
                while i >= d and a[p][i - d] > el:
                    a[p][i] = a[p][i - d]
                    i -= d
                a[p][i] = el
            d = 1 if d == 2 else int(d * 5.0 / 11)
    return a

def tournamentSort(array):
    arr = array.copy()
    for i in range(len(arr)):
        supportTournamentSortMethod(arr[i])
    return arr

def supportTournamentSortMethod(arr):
    t = [None] * 2 * (len(arr) + len(arr) % 2)
    index = len(t) - len(arr) - len(arr) % 2

    for i, v in enumerate(arr):
        t[index + i] = (i, v)

    for j in range(len(arr)):
        n = len(arr)
        index = len(t) - len(arr) - len(arr) % 2
        while index > -1:
            n = (n + 1) // 2
            for i in range(n):
                i = max(index + i * 2, 1)
                if t[i] != None and t[i + 1] != None:
                    if t[i][1] < t[i + 1][1]:
                        t[i // 2] = t[i]
                    else:
                        t[i // 2] = t[i + 1]
                else:
                    t[i // 2] = t[i] if t[i] != None else t[i + 1]
            index -= n

        index, x = t[0]
        arr[j] = x
        t[len(t) - len(arr) - len(arr) % 2 + index] = None

def quickSort(a):
    b = a.copy()
    for i in range(len(b)):
        supportQuickSortMethod(0, len(b[i]) - 1, b, i)
    return b

def supportQuickSortMethod(anotherFirst, anotherLast, array, row):
    first = int(anotherFirst)
    last = int(anotherLast)
    middle = int((first + last) / 2)

    while (first < last):

        while (array[row][first] < array[row][middle]):
            first += 1
        while (array[row][last] > array[row][middle]):
            last -= 1
        if (first <= last):
            array[row][first], array[row][last] = array[row][last], array[row][first]
            first += 1
            last -= 1

    if (anotherFirst < last):
        supportQuickSortMethod(anotherFirst, last, array, row)
    if (first < anotherLast):
        supportQuickSortMethod(first, anotherLast, array, row)

def supportPyramidSortMethod(a, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and a[i] < a[l]:
        largest = l

    if r < n and a[largest] < a[r]:
        largest = r

    if largest != i:
        a[i], a[largest] = a[largest], a[i]

        supportPyramidSortMethod(a, n, largest)

def pyramidSort(b):
    a = b.copy()
    for i in range(len(a)):
        n = len(a[i])

        for j in range(n, -1, -1):
            supportPyramidSortMethod(a[i], n, j)

        for j in range(n-1, 0, -1):
            a[i][j], a[i][0] = a[i][0], a[i][j]
            supportPyramidSortMethod(a[i], j, 0)
    return a

s = input()
if (s != ''):
    M = [0, 0, 0, 0]
    i = 0
    j = 0
    while i < len(s):
        s_int = ''
        flag = False
        while '0' <= s[i] <= '9' or s[i] == '-':
            if s[i] == '-':
                flag = True
            else:
                s_int += s[i]
            i += 1
            if i >= len(s):
                break
        i += 1
        M[j] = int(s_int)
        if flag:
            M[j] *= -1
        j += 1
    arrayExample = generateArray(M[0], M[1], M[2], M[3])
else:
    arrayExample = generateArray()
startTime = timeit.default_timer()
selectionSort(arrayExample)
print("Время работы сортировки выбором: " + str(timeit.default_timer() - startTime))

startTime = timeit.default_timer()
insertionSort(arrayExample)
print("Время работы сортировки вставкой: " + str(timeit.default_timer() - startTime))

startTime = timeit.default_timer()
exchangeSort(arrayExample)
print("Время работы сортировки обменом: " + str(timeit.default_timer() - startTime))

startTime = timeit.default_timer()
shellsSort(arrayExample)
print("Время работы сортировки Шелла: " + str(timeit.default_timer() - startTime))

startTime = timeit.default_timer()
tournamentSort(arrayExample)
print("Время работы турнирной сортировки: " + str(timeit.default_timer() - startTime))

startTime = timeit.default_timer()
pyramidSort(arrayExample)
print("Время работы сортировки пирамидальной сортировка: " + str(timeit.default_timer() - startTime))

startTime = timeit.default_timer()
quickSort(arrayExample)
print("Время работы быстрой сортировки: " + str(timeit.default_timer() - startTime))

mas = arrayExample.copy()
startTime = timeit.default_timer()
mas.sort()
print("Время работы встроенной сортировки: " + str(timeit.default_timer() - startTime))