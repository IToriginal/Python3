#평균 구하기
# 나의 코드
def solution(arr):
    return sum(arr)/len(arr)
# 테스트 코드
print(solution(arr=[1,2,3,4]))
print(solution(arr=[5, 5]))

# 다른 사람 코드
def average(list):
    return sum(list) / len(list)
# 테스트 코드
list = [5,5] 
print("평균값 : {}".format(average(list)));
