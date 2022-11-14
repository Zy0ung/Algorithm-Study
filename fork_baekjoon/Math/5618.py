import sys

#def gcd(a,b): #최대공약수
#    for i in range(min(a, b), 0, -1):
#        if (a % i == 0) and (b % i == 0):
#            return  i

#유클리드 호제법
#2개의 자연수 a, b에 대해서 b를 a로 나눈 나머지를 r이라고 하면 단(a < b), a와 b의
#최대 공약수는 a와 r의 최대공약수와 같다.
def gcd(a, b):
    if(a == 0):
        return b
    return gcd(b % a, a)

n = int(sys.stdin.readline()) #자연수 n개 2 또는 3
s = list(map(int, sys.stdin.readline().split())) #공약수를 구해야하는 자연수 n개

G = gcd(s[0], gcd(s[1], s[-1])) #2~3개의 자연수의 최대공약수

#최대공약수의 약수를 구하기
for i in range(1, (G//2)+1): #최대공약수의 반만큼 검사하여 약수를 구해준다 -> 이래야 시간초과가 안된다ㅜㅜ..
    if G % i == 0: #나눴을 때 나머지가 0이면 약수
        print(i)
print(G)