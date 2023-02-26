#짝수와 홀수

# 내 풀이
def solution(num):
    if num % 2 == 0:
        answer = "Even"
    else:
        answer = "Odd"
    return answer

#아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : " + solution(3))
print("결과 : " + solution(2))

# 다른 사람의 풀이
def evenOrOdd(num):
    if num % 2:
        return "Odd"
    return "Even"

print("결과 : " + evenOrOdd(3))
print("결과 : " + evenOrOdd(2))