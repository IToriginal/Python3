#1. 부서별 신청 금액 = d 이다. 많은 부서에 물품을 지원하기 위해 신청금액이 적은 순으로 정렬한다.
#2. 가장 적은 금액을 신청한 부서부터 예산에서 가능한 범위의 금액을 지원하여 주고 예산 가격을 줄이는 방법을 반복한다.
#3. 예산으로 더 이상 지원이 불가능하면 지원받은 부서의 수를 반환한다.

def solution(d, budget):
    answer = 0 #answer: 지원 받은 부서의 수
    d.sort()
    for i in range(len(d)):
        if d[i] <= budget:
            answer += 1
            budget -= d[i]
        else:
            break
    return answer