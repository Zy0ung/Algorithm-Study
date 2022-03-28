N, K = map(int, input().split())

M = []

for i in range(1, N+1):
    if (N % i) == 0:
        M.append(i)

if len(M) < K:
    print('0')
else:
    print(M[K-1])