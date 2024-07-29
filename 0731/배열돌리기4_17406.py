'''
배열 돌리는 연산 횟수가 6이하이므로 완전탐색 가능

배열돌려주는 함수 - return array
마지막에 행별로 합 더해서 최솟값 구해주는 함수

접근 1) - 1240ms
값을 뽑아서 덱으로 표현하고 rotate 이후 popleft 하면서 값 채우기
접근 2) - 3708ms
값을 뽑아서 한번에 다음 칸에 전달 (array copy 해야함)
'''

import sys
input = sys.stdin.readline
from itertools import permutations
from copy import deepcopy

def rotate_array(before_array, rotate_info):
    r,c,s = rotate_info
    after_array = deepcopy(before_array)
    for i in range(1, s+1):
        start_x, start_y = r-i,c-i
        end_x, end_y = r+i, c+i
        for dy in range(2*i):
            after_array[start_x][start_y+dy+1] = before_array[start_x][start_y+dy]  
        for dx in range(2*i):
            after_array[start_x+dx+1][end_y] = before_array[start_x+dx][end_y]
        for dy in range(2*i,0,-1):
            after_array[end_x][start_y+dy-1] = before_array[end_x][start_y+dy]
        for dx in range(2*i,0,-1):
            after_array[start_x+dx-1][start_y] = before_array[start_x+dx][start_y]
    return after_array

def find_minimum(array):
    value = int(1e5)
    for i in array[1:-1]:
        value = min(value, sum(i))
    return value
        
N, M ,K = map(int, input().split())
array_ori = [[0]*(M+2)] + [[0]+list(map(int, input().split()))+[0] for _ in range(N)] + [[0]*(M+2)]
rotate_info = [list(map(int, input().split())) for _ in range(K)]
minimum = int(1e5)

for order in list(permutations(range(K),K)):
    array = deepcopy(array_ori)
    for o in order:
        array = rotate_array(array, rotate_info[o])
    minimum = min(minimum, find_minimum(array))

print(minimum)