"""
deque는 스택과 큐의 기능을 모두 갖고 있는 객체로, 출입구를 양쪽으로 갖고 있다.
따라서 스택처럼 쓸 수 있고, 큐처럼 쓸 수 있다.
"""
from collections import deque
dq = deque('love')
# dq -> 출력: deque(['l','o','v','e'])
# 문자열을 이용해 deque를 만들면 각 문자가 요소로 된 리스트 형태의 deque가 만들어진다.

"""
1. 스택 구현: append(), pop()
  스택은 마지막(오른쪽 끝)에서 입출력한다.
  입력: append() / 출력: pop()
"""
dq.append('m')
# -> deque(['l','o','v','e', 'm'])
dq.pop()
# -> 'm'
dq
# -> deque(['l','o','v','e'])

"""
2. 큐 구현: appendleft(), pop(), append(), popleft()
  큐는 왼쪽(처음)애서 입력되고, 오른쪽(마지막)으로 출력된다.
  입력: appendleft() / 출력: pop()
  (반대로 오른쪽 입력, 왼쪽 출력의 경우 - 입력: append() / 출력: popleft())
"""
dq.appendleft('I')
# -> deque(['I', 'l','o','v','e'])
dq.pop()
# -> 'e'
dq
# -> deque(['I', 'l','o','v'])

"""
3. deque 확장: extend(), extendleft()
  deque의 오른쪽 확장: extend()
  왼쪽 확장: extendleft()
"""
dq
# -> deque(['l','o','v','e'])
dq.extend('you')
dq
# -> deque(['l','o','v','e', 'y', 'o', 'u'])
dq.extendleft('I')
dq
# -> deque(['I', 'l','o','v','e', 'y', 'o', 'u'])


