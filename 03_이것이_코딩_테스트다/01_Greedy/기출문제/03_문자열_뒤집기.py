num = map(int, input())
num_list_0 = list(num)
num_list_1 = num_list_0.copy()
result_0, result_1 = 0, 0

for i in range(len(num_list_0)):
    if i == 0:
        continue
    if i == len(num_list_0) - 1:
        if num_list_0[i] == 1:
            num_list_0[i] = 0
            result_0 += 1
            break
    if num_list_0[i] != num_list_0[i - 1]:
        if num_list_0[i - 1] == 1:
            num_list_0[i - 1] = 0
            result_0 += 1
            
for i in range(len(num_list_1)):
    if i == 0:
        continue
    if i == len(num_list_1) - 1:
        if num_list_1[i] == 0:
            num_list_1[i] = 1
            result_1 += 1
            break
    if num_list_1[i] != num_list_1[i - 1]:
        if num_list_1[i - 1] == 0:
            num_list_1[i - 1] = 1
            result_1 += 1
    

print(min(result_1, result_0))
# 이럴 필요없이 한번 반복하면서 1과 0을 모두 카운트할 수 있었다...
# 효율적인 방법을 더 생각해보고 코드짜기!!!
