T = int(input())

for i in range(T):
    A, B = map(int, input().split())
    print("Case #", end='')
    print(i+1, end=': ')
    print(A, "+", B, "=", A+B)
    i += 1