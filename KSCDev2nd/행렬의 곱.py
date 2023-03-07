# NumPy 라이브러리 사용
import numpy as np #NumPy 라이브러리 사용

def solution(arr1, arr2):
		# arr1과 arr2를 NumPy 행렬로 변환한다.
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)

		#행렬의 곱셉을 수행하여 결과를 반환한다.
    result = np.dot(arr1, arr2)

		#NumPy 배열을 리스트로 변환하여 반환한다.
    return result.tolist()

print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))