import sys

def input():
    return sys.stdin.readline().strip()


T = int(input())

for a in range(T):
    stack = []
    s = input()

    for i in s:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack):
                stack.pop()
            else:
                print("NO")
                break

    else: #break문으로 끊기지 않고 수행됐을경우 수행
        if stack:
            print("NO")
        else:
            print("YES")