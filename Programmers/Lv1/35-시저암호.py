#(1) 26보다 작을 경우 26으로 나눈 나머지는 그 숫자 자체이고 (예) 5%26 -> 5)
#(2) 26 이상일 경우 26으로 나눈 나머지를 활용하면 다시 문자열 처음으로 돌아가 활용 가능하다. (예) 26%26 -> 0, a / A를 의미)

def solution(s, n):
    low = "abcdefghijklmnopqrstuvwxyz" #인덱스는 0 ~ 25
    up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    answer = ''
    for char in s:
        if char in low:
            index = low.find(char) + n #low 문자열에서 찾은 해당 알파벳 인덱스 + n
            answer += low[index % 26] #26으로 나눈 나머지를 사용할 경우 25를 초과하는 경우도 활용
        elif char in up:
            index = up.find(char) + n
            answer += up[index % 26]
        else:
            answer += " " #공백의 경우도 고려
    return answer