# sorted 함수
"""
- 기존의 리스트를 변경하는 것이 아니라 정렬의 새로운 리스트를 반환한다.
- 어떤 이터러블 객체도 받을 수 있다 (ex 딕셔너리 객체도 받을 수 있음)
- 오름차순 정렬 : sorted()
- 내림차순 정렬 : sorted(reverse=True)
"""

# sorted 함수 - key 인자
"""
오름차순 정렬 : sorted(a, key=lambda x:x[0])
내림차순 정렬 : sorted(a, key=lambda x:-x[0])
-> '-' 마이너스만 붙여주면 내림차순으로 만들 수 있다.
-> 요소가 여러개일 경우 각 요소마다 정렬기준을 정해줄 수 있다. sorted(a, key=lambda x: (x[0], -x[1])
-> '-' 말고 reverse=True로 내림차순을 만들 수 있다.
"""

students = [
        ('홍길동', 3.9, 2016303),
        ('김철수', 3.0, 2016302),
        ('최자영', 4.3, 2016301),
]

sorted(students, key=lambda student: student[2])
# 결과: [('최자영', 4.3, 2016301), ('김철수', 3.0, 2016302), ('홍길동', 3.9, 2016303)]

sorted(students, key=lambda student: student[2], reverse=True)
# 결과: [('홍길동', 3.9, 2016303), ('김철수', 3.0, 2016302), ('최자영', 4.3, 2016301)]



# sort() 메소드
"""
- 리스트를 정렬된 상태로 변경
- 리스트만을 위한 메소드
- 오름차순 정렬 : sort()
- 내림차순 정렬 : sort(reverse=True)
"""
a = [1, 10, 5, 7, 6]
a.sort()
# 결과: [1, 5, 6, 7, 10]

a = [1, 10, 5, 7, 6]
a.sort(reverse=True)
# 결과: [10, 7, 6, 5, 1]
