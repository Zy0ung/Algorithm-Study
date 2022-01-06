h_s = int(input())
s_p = int(input())
p_a = int(input())
a_h = int(input())

sec = h_s + s_p + p_a + a_h

m = sec//60
s = sec % 60

print(m)
print(s)