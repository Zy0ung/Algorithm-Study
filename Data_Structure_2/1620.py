from sys import stdin

def input():
    return stdin.readline().rstrip()

N, M = map(int, input().split())

dict_name = {}
dict_int = {}

for i in range(1, N + 1):
    pokemon = input()
    dict_name[pokemon] = i
    dict_int[i] = pokemon

for _ in range(M):
    q = input().rstrip()
    if q.isdigit(): #.isdigit()문자열이 숫자로만 이루어져있는지 확인하는 함수
        print(dict_int[int(q)])
    else:
        print(dict_name[q])