r, g, b = map(int,input().split())
n = 0

for i in range(r):
    for j in range(g):
        for k in range(b):
            print('%d %d %d' % (i, j, k))
            n += 1
print(n)