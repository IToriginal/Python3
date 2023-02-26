#자릿수 더하기
# 내 코드
def solution(n):
    a=list(map(int, str(n)))
    return sum(a)
print("내 결과 : {}".format(solution(1236)));

# 다른 사람의 코드 (1)
def sum_digit(number):
    return sum([int(i) for i in str(number)])
print("다른 사람 결과(1) : {}".format(sum_digit(123)));


# 다른 사람의 코드(2: 재귀)
def sum_digit(number):
    '''number의 각 자릿수를 더해서 return하세요'''
    if number < 10:
        return number

    return number%10 + sum_digit(number//10)

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("다른 사람 결과(2) : {}".format(sum_digit(123)));
