import sys
from collections import deque

N = int(input())

queue = deque([]) #시간복잡도를 고려해 deque를 사용

for i in range(N):
    cmd = sys.stdin.readline().split()
    
    if cmd[0] == 'push':
        queue.append(int(cmd[1]))
    
    elif cmd[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft()) #큐의 원소 제거

    elif cmd[0] == 'size':
        print(len(queue))
    
    elif cmd[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    elif cmd[0] == 'front' :
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    
    elif cmd[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])