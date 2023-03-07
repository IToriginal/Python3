def solution(s):
    n = len(s)
    #문자열이 없거나 한자리의 문자열 값만 가질 경우
    if n == 0:
        return ""
    elif n == 1:
        return s
    
    start, end = 0, 0
    for i in range(n):
        len1 = search(s, i, i)
        len2 = search(s, i, i+1)
        length = max(len1, len2)
        if length > end - start:
            start = i - (length - 1) // 2
            end = i + length // 2
    return s[start:end+1]
    
def search(s, left, right):
    L, R = left, right
    while L >= 0 and R < len(s) and s[L] == s[R]:
        L -= 1
        R += 1
    return R - L - 1

print(solution("babad"))
print(solution("cbbd"))