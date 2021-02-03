# 2중 for문을 피하려고 if문을 다룬 틀을 만들었지만 실패해서 시간 소요가 길어짐
# 쉽게 할 수 있는 부분부터 먼저해보고 나서 효율성이 높은 다른 방법을 검토해보도록 하기
def solution(brown, yellow):
    answer, res = [], []
    ans = brown + yellow    

    # for문 range 설정에 i = 1인 경우는 필요없다. (i = 1인 경우가 아예 없기 때문)
    for i in range(2, (brown // 2 + 2)):
        if ans % i == 0:
            answer.append(i)

    for i in answer:
        for j in answer:
            if i * j == ans:
                if (i - 2) * (j - 2) == yellow:
                    res.append(i)
                    res.append(j)
                    print(res)
                    break
        if res != []:
            break

    res.sort(reverse = True)
    return res
    
    
    
    
   # 다른 사람의 풀이
   def solution(brown, red):
    for i in range(1, int(red**(1/2))+1):
        if red % i == 0:
            if 2*(i + red//i) == brown-4:
                return [red//i+2, i+2]
