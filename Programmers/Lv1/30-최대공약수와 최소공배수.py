import math
def solution(n, m):
    answer = []
    # 최대공약수
    for i in range(min(n,m),0,-1): 
        if n%i ==0 and m%i==0:
            answer.append(i)
            break

    # 최소공배수
    for i in range(max(n,m),n*m+1):
        if i%n == 0 and i%m == 0:
            answer.append(i)
            break
    return answer

#유클리드 호제법
#최대공약수
def GCD(x,y):
    while(y): #y가 참일 동안 = 자연수일 때 = a % b != 0
        x, y = y, x % y
    return x

print(GCD(10, 12)) #2

#최소공배수
def LCM(x,y):
    result = (x*y) // GCD(x,y)
    return result

print(LCM(10, 12)) #60


# 파이썬 3.9 이상 사용 가능: lcm 사실상 코테에서는 사용 불가능
import math

def solution(n, m):
    answer = [math.gcd(n, m), math.lcm(n, m)]
    return answer

print(solution(3, 12))