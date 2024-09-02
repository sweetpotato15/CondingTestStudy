import sys
input = sys.stdin.readline
import heapq

N = int(input())
array = []
for i in range(N):
    num = int(input())
    heapq.heappush(array, num)

ans = 0

while len(array) > 1:
    a = heapq.heappop(array)
    b = heapq.heappop(array)
    heapq.heappush(array, a+b)
    ans += a+b

print(ans)
