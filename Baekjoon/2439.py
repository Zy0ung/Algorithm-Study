N = int(input())

j = 1
for i in range(N, 0, -1):
    print(' '*(i-1), end='')
    print('*'*(j))
    j+=1