#이미지의 가로 해상도 w, 세로 해상도 h, 한 픽셀을 저장하기 위한 비트 b 가 주어질 때,
#압축하지 않고 저장하기 위해 필요한 저장 용량을 계산하는 프로그램을 작성해 보자.

w, h, b = input().split()

save = float(w)*float(h)*float(b)/8/1024/1024

print(format(float(save),".2f"),end=" ")
print("MB")

