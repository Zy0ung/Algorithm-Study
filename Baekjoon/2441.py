N = int(input())

j = 0
for i in range(N, 0, -1):
    print(' ' *(j), end='')
    print('*'*i)
    j += 1