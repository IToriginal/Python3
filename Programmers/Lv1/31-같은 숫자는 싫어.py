#빈 배열 answer 을 만들어주고 배열을 순차적으로 append 함.
#전 인덱스 값과 비교하여 다른 경우에만 append
def solution(arr):
    answer = []
    for i in range(len(arr)):
        if i == 0:
            answer.append(arr[i])
        elif arr[i] != arr[i-1]:
            answer.append(arr[i])
    return answer