#3항 연산 사용하기
a, b = input().split()
a = int(a)
b = int(b)
c = (a if (a >= b) else b)
print(int(c))