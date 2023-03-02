def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3) #문자열을 3진수로 생성
    return answer

#divmod() 함수: 몫과 나머지를 구하는 방법 (리턴 값이 2개)
def solution(n):
    answer = ''

    while n >= 1:
        n, rest = divmod(n, 3)
        answer += str(rest)
    answer = int(answer, 3)

    return answer