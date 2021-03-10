num = map(int, input())
num_list = list(num)
num_list.sort()

result = 0
for num in num_list:
    if num == 0 or num == 1:
        result += num
    else:
        if result == 0 or result == 1:
            result += num
        else:
            result *= num
            
print(result)
