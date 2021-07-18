#출석 번호를 n번 무작위로 불렀을 때, 각 번호(1 ~ 23)가 불린 횟수를 각각 출력해보자.

n = int(input())      #개수를 입력받아 n에 정수로 저장
a = input().split()  #공백을 기준으로 잘라 a에 순서대로 저장

for i in range(n) : 
  a[i] = int(a[i])       #a에 순서대로 저장되어있는 각 값을 정수로 변환해 다시 저장

d = []
for i in range(24) :
  d.append(0)

for i in range(n) :    #번호를 부를 때마다, 그 번호에 대한 카운트 1씩 증가
  d[a[i]] += 1

for i in range(1, 24) :  #카운트한 값을 공백을 두고 출력
  print(d[i], end=' ')