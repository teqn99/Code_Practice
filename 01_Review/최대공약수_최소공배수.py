# 최대공약수 
def gcd(x, y):
  # y가 0이 될 때까지 반복
  while y:
    # y를 x에 대입
    # x를 y로 나눈 나머지를 y에 대입
    x, y = y, (x % y)
  return x
  
# 파이썬에서는 최대공약수는 from math import gcd로 최대공약수 함수 사용가능
  
  
  
# 최소공배수
from math import gcd
def lcm(x, y):
  return (x * y) // gcd(x, y)
  
# N개의 최소공배수
from math import gcd
def solution(arr):
    def lcm(x, y):
        return (x * y) // gcd(x, y)

    while True:
        arr.append(lcm(arr.pop(), arr.pop()))
        if len(arr) == 1:
            return arr[0]

    return answer
