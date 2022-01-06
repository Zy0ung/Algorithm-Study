num = int(input())

def plus(num):
    n = 0
    for i in range(num, 0, -1):
        n += i
    print(n)

plus(num)