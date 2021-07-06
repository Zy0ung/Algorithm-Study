#3개의 정수(a, b, c)가 입력되었을 때, 짝수만 출력해보자.

a, b, c = input().split()

if int(a) % 2 ==0:
    print(int(a))

if int(b) % 2 ==0:
    print(int(b))

if int(c) % 2 ==0:
    print(int(c))   