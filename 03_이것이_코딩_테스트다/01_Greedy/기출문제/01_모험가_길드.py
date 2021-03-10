n = map(int, input())
member_list = list(map(int, input().split()))
group = []
group_size = 0

member_list.sort()
for member in member_list:
    if member == 1:
        group.append(member)
    else:
        group_size += 1
        if group_size == member:
            group_size = 0
            group.append(member)
            
print(len(group))
