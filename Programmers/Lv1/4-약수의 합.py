#약수의 합
# 나의 코드
def solution(n):
    sum = 0
    if n == 0:
        answer = 0
        return answer
    for i in range(1, n+1):
        if n % i == 0:
            sum += i
        answer = sum
    return answer

print(solution(12))
print(solution(5))

# 다른 사람의 코드🌟
def sumDivisor(num):
    # num / 2 의 수들만 검사하면 성능 약 2배 향상
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])

print(sumDivisor(12))
print(sumDivisor(5))
