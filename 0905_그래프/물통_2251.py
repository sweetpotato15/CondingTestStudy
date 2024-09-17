import sys
input = sys.stdin.readline
from collections import deque

water = [0] + list(map(int, input().split()))
array = [0]*3 + [water[-1]]

# A, B, C -> 1, 2, 3
start = [1, 1, 2, 2, 3, 3]
end = [2, 3, 1, 3, 1, 2]
answer = [False] * 201 # A가 0일때 C에 가능한 물의 양

q = deque([[4], [5]])
answer[array[-1]] = True
while q:
    index = q.popleft()
    # 넘쳐 흐르는 경우
    if array[end[index]] + array[start[index]] >= water[end[index]]:
        array[end[index]], array[start[index]] = water[end[index]]
        array[start[index]] -= 
    # 아닌 경우
    else:
        array[end[index]] += array[start[index]]
        array[start[index]] = 0
    