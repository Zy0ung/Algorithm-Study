person, party = input().split()

#각 기사에 실려있는 참가자의 수
A, B, C, D, E = input().split()

#파티에있던 사람 수
real_person = int(person) * int(party)

A = int(A) - real_person
B = int(B) - real_person
C = int(C) - real_person
D = int(D) - real_person
E = int(E) - real_person

print(A, B, C, D, E)