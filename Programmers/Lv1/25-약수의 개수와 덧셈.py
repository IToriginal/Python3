def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5: #i**0.5는 i의 제곱근을 구하는 식. 제곱근이 정수로 표현 가능한 수는 약수의 개수가 홀수 개
            answer -= i
        else:
            answer += i
    return answer