import sys
input = sys.stdin.readline
from copy import deepcopy

N, M = map(int, input().split())
array = [[0]*(N+1)] + [[0]+list(map(int, input().split())) for _ in range(N)]
sum_array = [[0]*(N+1) for _ in range(N+1)] # [i][j] : [0][0]부터 [i][j]까지의 합

for i in range(1,N+1):
    for j in range(1,N+1):
        sum_array[i][j] = sum_array[i-1][j] + sum_array[i][j-1] - sum_array[i-1][j-1] + array[i][j]

for _ in range(M):
    x1,y1,x2,y2 = map(int, input().split())
    ans = sum_array[x2][y2] - sum_array[x1-1][y2] - sum_array[x2][y1-1] + sum_array[x1-1][y1-1]
    print(ans)