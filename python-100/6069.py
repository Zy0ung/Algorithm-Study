#평가를 문자(A, B, C, D, ...)로 입력받아 내용을 다르게 출력해보자.
#평가 내용
#평가 : 내용
#A : best!!!
#B : good!!
#C : run!
#D : slowly~
#나머지 문자들 : what?

estimate = input()

if estimate == 'A':
    print('best!!!')
elif estimate == 'B':
    print('good!!')
elif estimate == 'C':
    print('run!')
elif estimate == 'D':
    print('slowly~')
else:
    print('what?')