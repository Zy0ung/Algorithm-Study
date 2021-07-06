#입력된 두 정수(a, b) 중 큰 값을 출력하는 프로그램을 작성해보자.
#단, 3항 연산을 사용한다.

a, b = input().split()

if int(a) > int(b) :
    print(int(a))
elif int(a) < int(b) :
    print(int(b))