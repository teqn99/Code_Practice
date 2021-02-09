# 나의 풀이
def solution(progresses, speeds):
    answer = []
    n, m, tf = 0, 0, False    # n: 지난 날짜의 수, m, tf: 체크 포인트

    for i, v in enumerate(progresses):
        ans = v + n*speeds[i]
        if ans >= 100: 
            m += 1
            if i == len(progresses) - 1:
                answer.append(m)
            continue

        if tf != False:
            answer.append(m)
            m, tf = 0, False

        while tf == False:
            ans += speeds[i]
            n += 1
            if ans >= 100:
                m += 1
                tf = True
                if i == len(progresses) - 1:
                    answer.append(m)

    return answer
    
    
    
# 다른 사람의 풀이
def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]
    
# zip함수 더 자주 사용해보도록 익혀보기


