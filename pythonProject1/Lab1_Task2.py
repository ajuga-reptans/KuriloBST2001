import random

s = input()
M = [50, 50, -250, 1011]
if (s != ''):
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
Matrix = [[random.randint(M[2], M[3]) for i in range(M[0])] for i in range(M[1])]

for i in range(M[1]):
    for j in range(M[0]):
        print(Matrix[i][j], end = ' ')
    print()