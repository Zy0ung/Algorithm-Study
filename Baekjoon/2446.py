N = int(input())

for i in range(1, N+1):
    print(' ' * (i - 1) + '*' * (2 * (N-i) + 1))

for k in range(1, N):
    print(' ' * (N - k - 1)+ '*' * ((2 * k) + 1))