#풀이(1)
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer


#풀이(2)
def solution(left, right):
    result = 0
    for i in range(left, right + 1):
        result += dividor(i)
    return result

def dividor(n):
    result = len([i for i in range(1, n+1) if not n%i])
    return -n if result%2 else n