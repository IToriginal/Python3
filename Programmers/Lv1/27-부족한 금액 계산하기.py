#산술 평균을 활용한 풀이법
# price * 1 + price * 2 + price * 3 + price * 4 ...
# = price(1+2+3+4+...)
# = price * (n(n+1)/2)

def solution(price, money, count):
    return max(0,price*(count+1)*count/2-money)

#가독성 좋은 코드
def readgood(price, money, count):
    pay = 0
    for i in range(1, count + 1):
        pay += (price * i)
    if money < pay:
        return pay - money
    else:
        return 0