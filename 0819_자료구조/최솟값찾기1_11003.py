'''
sol1) 길이가 L로 고정, 고정된 길이 속 최솟값 -> 슬라이딩윈도우
1) q에서 top(맨 오른쪽)에 존재하는 값이 현재 들어가려는 값보다 작을때까지 pop
2) 현재 값 append 하고, 왼쪽부터 index 유효한지 확인
3) ans 에 append

sol2) heap으로 구현 ..? -> heappush 할때 [] 로 넣는 것 보다 () 로 넣는 것이 더 빠름
'''
import sys
input = sys.stdin.readline
import heapq
from collections import deque

N, L = map(int, input().split())
array = list(map(int, input().split()))

ans = []
q = deque([[0, array[0]]]) # [index, value]
for i in range(N):
    while q and q[-1][1] >= array[i]: # q의 top의 value 가 들어가는 값보다 작을때까지
        q.pop()
    q.append([i, array[i]])
    while q[0][0] + L <= i:
        q.popleft()
    ans.append(q[0][1])

print(*ans)

## sol2)
# N, L = map(int, input().split())
# array = list(map(int, input().split()))

# ans = []
# q = []
# for i in range(N):
#     heapq.heappush(q, (array[i], i))
#     value = heapq.heappop(q)
#     while i >= value[1] + L:
#         value = heapq.heappop(q)
#     ans.append(value[0])
#     heapq.heappush(q, value)

# print(*ans)
