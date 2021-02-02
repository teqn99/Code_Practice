# map 함수 사용 안한 경우
a = [1.2, 2.5, 3.7, 4.6]
for i in range(len(a)):
    a[i] = int(a[i])
  
# map 함수 사용한 경우
a = [1.2, 2.5, 3.7, 4.6]
a = list(map(int, a))

# for문의 사용을 줄이고 효율성을 높이기 위해 map 함수를 사용하도록 익혀볼 것
