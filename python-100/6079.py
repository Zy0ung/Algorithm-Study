#1, 2, 3 ... 을 계속 더해 나갈 때,
#그 합이 입력한 정수(0 ~ 1000)보다 같거나 작을 때까지만
#계속 더하는 프로그램을 작성해보자.

n = int(input())
add = 0
i = 0
while True:
    i += 1
    add += i
    if (add >= n):
        print(i)
        break