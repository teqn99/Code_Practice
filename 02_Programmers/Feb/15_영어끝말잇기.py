# 나의 풀이
def solution(n, words):
    ans = 0  # 문제가 있는 지점의 index를 저장할 값
    w = []  # 사용된 단어들을 저장할 리스트

    for idx, val in enumerate(words):
        if idx == 0:
            w.append(val)
            continue
        else:  
            if (val[0] == words[idx - 1][-1]) and (val not in w):
                w.append(val)
                continue
            else:
                ans = idx
                break

    if ans == 0:
        return [0, 0]

    return [ans % n + 1, ans // n + 1]
    
# 잘한 것 같다!!
