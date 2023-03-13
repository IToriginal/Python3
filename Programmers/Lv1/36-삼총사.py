from itertools import combinations

def solution(number):    
    num_combinations = [sum(comb) for comb in list(combinations(number, 3)) if sum(comb) == 0]
    
    return len(num_combinations)

# TEST
number1 = [-2, 3, 0, 2, -5]
number2 = [-3, -2, -1, 0, 1, 2, 3]
number3 = [-1, 1, -1, 1]

result1 = solution(number1)
result2 = solution(number2)
result3 = solution(number3)

print(result1)
print(result2)
print(result3)

# 다른 코드
def solution (number) :
    from itertools import combinations
    cnt = 0
    for i in combinations(number,3) :
        if sum(i) == 0 :
            cnt += 1
    return cnt