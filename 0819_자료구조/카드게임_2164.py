'''
제일 위에 있는 카드 버린다 -> 그다음 위에 카드 맨 아래로
'''
from collections import deque

N = int(input())
array = deque(range(1, N+1))
while len(array) > 1:
    array.popleft()
    array.rotate(-1)
print(*array)