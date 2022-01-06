N = int(input())
numbers = list(map(int, input().split()))

count = 0

for n in numbers:
    if n != 1 :
        for i in range(2, n):
            if n % i == 0 :
                break
        else:
            count += 1
                

print(count)