def solution(s: str) -> int:
    start = end = 0  # 시작 포인터(start)와 끝 포인터(end)를 0으로 초기화합니다.
    n = len(s)  # 문자열의 길이를 구합니다.
    dic = {}  # 딕셔너리를 만들어서 문자열의 각 문자가 등장한 마지막 위치를 기록합니다.
    max_len = 0  # 중복 문자가 없는 가장 긴 부분 문자열의 길이를 저장할 변수를 초기화합니다.

    while end < n:  # 끝 포인터(end)가 문자열의 길이보다 작을 때까지 반복합니다.
        if s[end] not in dic or dic[s[end]] < start:  # 현재 문자가 딕셔너리에 없거나 현재 문자의 마지막 등장 위치가 시작 포인터보다 이전일 경우
            dic[s[end]] = end  # 딕셔너리에 현재 문자의 인덱스(end)를 저장합니다.
            end += 1  # 끝 포인터(end)를 한 칸씩 이동합니다.
            max_len = max(max_len, end - start)  # 구간의 길이를 갱신합니다.
        else:  # 현재 문자가 딕셔너리에 있고 현재 문자의 마지막 등장 위치가 시작 포인터 이후일 경우
            start = dic[s[end]] + 1  # 시작 포인터(start)를 현재 문자의 마지막 등장 위치 다음으로 이동합니다.
            dic[s[end]] = end  # 딕셔너리에 현재 문자의 인덱스(end)를 저장합니다.
            end += 1  # 끝 포인터(end)를 한 칸씩 이동합니다.

    return max_len  # 중복 문자가 없는 가장 긴 부분 문자열의 길이를 반환합니다.

#TEST
print(solution("abcabcbb"))
print(solution("bbbbb"))
print(solution("pwwkew"))