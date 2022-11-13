from collections import deque

N, K = map(int, input().split())

people = deque()
result = []

for i in range(N):
    people.append(i+1)

# <1, 2, 3, 4, 5, 6, 7>
while people:
    for _ in range(K-1):
        people.append(people.popleft())

    result.append(people.popleft())

print('<', end='')
print(str(result).strip('[').strip(']'), end='')
print('>')