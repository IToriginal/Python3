n = int(input())
snum = 0
sum = 0

while True:
    sum += snum
    snum += 1
    if sum >= n:
        break
print(sum)