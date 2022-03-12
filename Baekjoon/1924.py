x, y = map(int, input().split())

day = 0
A = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
B = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

for i in range(x-1):
    day += A[i]
day = (day+y) %7

print(B[day])