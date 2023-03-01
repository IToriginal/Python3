def solution(numbers):
    answer = 0
    for i in range(1, 10):
        if i not in numbers:
            answer += i
    return answer

#생각하지 못한 코드
def solution(numbers):
    return sum(range(10)) - sum(numbers)