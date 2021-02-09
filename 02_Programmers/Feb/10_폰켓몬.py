# 나의 풀이
def solution(nums):
    answer = [0]

    for i in range(len(nums)):
        if answer[-1] != nums[i]:
            if nums[i] not in answer:
                answer.append(nums[i])

        if len(answer[1:]) == (len(nums) // 2):
            break

    return len(answer[1:])
    
    
    
# 다른 사람의 풀이
def solution(ls):
    return min(len(ls)/2, len(set(ls)))
    
# ㅋㅋㅋㅋㅋ
# set함수 잊지말기
