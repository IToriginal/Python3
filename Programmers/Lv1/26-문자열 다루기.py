def solution(s):
    #isdigit() 함수는 문자열이 숫자로 구성되어 있는지를 판별해주는 함수이다.
    #하지만, 음수나 소수점의 경우는 숫자임에도 False를 리턴한다.
    if (len(s) == 4 or len(s) == 6) and s.isdigit() == True:
        return True
    else:
        return False
    
# 다른 사람의 풀이
def othercode(s):
    return s.isdigit() and len(s) in [4,6]