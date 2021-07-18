#출석 번호를 n번 무작위로 불렀을 때, 가장 빠른 번호를 출력해 보자.

n = int(input())

a = input().split()

for i in range(n) : 
  a[i] = int(a[i])

d = []

for i in range(n) :
  d.append(a[i])

print(min(d))