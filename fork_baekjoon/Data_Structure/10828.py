# push X : 정수 X를 스택에 넣는 연산
# pop : 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력. 만약 스택에 들어있는 정수가 없는 경우는 -1을 출력
# size : 스택에 들어있는 정수의 개수 출력
# empty : 스택이 비어있으면 1, 아니면 0을 출력
# top : 스택의 가장 위에 있는 정수 출력. 만약 스택에 들어있는 정수가 없는 경우 -1 출력

import sys

N = int(input())

Stack = []

for i in range(N):
    cmd = list(map(str, sys.stdin.readline().split()))
    
    if cmd[0] == 'push':
        Stack.append(int(cmd[1]))
    
    elif cmd[0] == 'pop':
        if len(Stack)==0:
            print(-1)
        else:
            print(Stack.pop())

    elif cmd[0] == 'size':
        print(len(Stack))
    
    elif cmd[0] == 'empty':
        print(0 if len(Stack) else 1)

    elif cmd[0] == 'top':
        if len(Stack) == 0:
            print(-1)
        else:
            print(Stack[-1])