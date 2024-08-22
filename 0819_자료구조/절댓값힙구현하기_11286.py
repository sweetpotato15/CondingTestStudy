import sys
input = sys.stdin.readline
import heapq

N = int(input())
q = []
for _ in range(N):
    x = int(input())
    if x != 0:
        heapq.heappush(q, (abs(x),x))
    else:
        if not q:
            print(0)
        else:
            value = heapq.heappop(q)
            print(value[1])