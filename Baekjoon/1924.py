#월에 따른 일 수
A = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#요일
B = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
#요일을 계산하기 위한 변수
DAY = 0

X, Y = map(int, input().split())

for i in range(X-1):
    DAY = DAY + A[i]
DAY = (DAY + Y) % 7

print(B[DAY])