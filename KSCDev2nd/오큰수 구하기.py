def solution(arr):
    n = len(arr)
    result = [-1] * n
    stack = []
    for i in range(n):
        while stack and arr[stack[-1]] < arr[i]:
            result[stack.pop()] = arr[i]
        stack.append(i)
    return result

#TEST
print(solution([3, 5, 2, 7]))
print(solution([9, 5, 4, 8]))