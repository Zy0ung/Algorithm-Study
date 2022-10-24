A = int(input())
B = int(input())
C = int(input())

result = list(str(A * B * C))

count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in result:
    count[int(i)] += 1

for c in count:
    print(c)