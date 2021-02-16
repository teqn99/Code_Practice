# 나의 풀이
def solution(skill, skill_trees):
    answer = 0
    skills = []  # skill을 하나하나씩 담을 배열

    for i in skill:
        skills.append(i)

    for j in skill_trees:  # j: skill_trees 내의 단어 
        a = []
        number = 0
        for k in j:  # k: 단어 내의 한 글자씩
            if k in skills:
                if k == skills[number]:
                    a.append(k)
                    number += 1
                else:
                    break
            else:
                a.append(k)

        if len(a) == len(j):  # 완성된 글자와 원래 글자를 비교해서 같으면 answer + 1을 해주는 것
            answer += 1

    return answer
   
   
   
# 다른 사람의 풀이
def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_list = list(skill)

        for s in skills:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            answer += 1

    return answer

# 나도 잘한 것 같지만 pop를 쓸 수도 있다는 걸 생각해보기
