#입력된 세 정수 a, b, c 중 가장 작은 값을 출력하는 프로그램을 작성해보자.
#단, 3항 연산을 사용한다.

a,b,c = input().split()

if int(a) > int(b) and int(b) >int(c):
    print(int(c))
elif int(a) > int(b) and int(b) < int(c):
    print(int(b))
elif int(a) < int(b) and int(a) < int(c):
    print(int(a))
elif int(a) < int(b) and int(a) > int(c):
    print(int(c))
else:
    print(int(a))