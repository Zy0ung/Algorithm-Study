from collections import deque

N = int(input())

cards = deque([])

for i in range(N):
    cards.append(i+1)

while len(cards) != 1:
    cards.popleft()
    cards.append(cards.popleft())


print(cards.pop())