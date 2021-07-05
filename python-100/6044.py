#정수 2개(a, b)를 입력받아 합, 차, 곱, 몫, 나머지, 나눈 값을 자동으로 계산해보자.
#단 0 <= a, b <= 2147483647, b는 0이 아니다.

a, b = input().split()

add = (int(a)+int(b))
sub = (int(a)-int(b))
mul = (int(a)*int(b))
par = (int(a)//int(b))
rem = (int(a)%int(b))
div = (int(a)/int(b))

print(add)
print(sub)
print(mul)
print(par)
print(rem)
print(format(div, ".2f"))