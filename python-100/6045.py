#정수 3개를 입력받아 합과 평균을 출력해보자.

a,b,c = input().split()

add = (int(a)+int(b)+int(c))

average = (float(add/3))

print(add, end=" ")
print(format(average, ".2f"))