import sys
input = sys.stdin.readline
import copy
'''
사무실 크기 최대 8*8 이고 CCTV 개수가 최대 8개이므로 백트래킹 고려 
CCTV 위치를 받아서 각각의 경우 백트래킹 

오른쪽 0 위 1 왼쪽 2 아래 3
cctv_type 별 화살표 : [0],[0,2],[0,1],[0,1,2],[0,1,2,3]

백트래킹 
- 종료조건 : n == cctv 개수
- 반복 구조 : 가능한 방향을 완전 탐색


'''

N, M = map(int, input().split())
graph = [[6]*(M+2)] + [[6]+list(map(int, input().split()))+[6] for _ in range(N)] +[[6]*(M+2)]

cctv = [] # cctv 정보
direction = [[],
             [[0],[1],[2],[3]],
             [[0,2],[1,3]],
             [[0,1],[1,2],[2,3],[3,0]],
             [[0,1,2],[1,2,3],[2,3,0],[3,0,1]],
             [[0,1,2,3]]]

for i in range(1, N+1):
    for j in range(1,M+1):
        if 1 <= graph[i][j] <= 5:
            cctv.append([graph[i][j], i,j]) # cctv 타입, x좌표, y좌표

cctv_num = len(cctv)
answer = N*M # 사각지대 개수
dx = [0,-1,0,1]
dy = [1,0,-1,0] # 우,상,좌,하

def working_cctv(dir, x,y, lst): # cctv num, lst
    for i in dir:
        cx = x
        cy = y
        while True:
            cx += dx[i]
            cy += dy[i]
            if lst[cx][cy] == 6:
                break
            lst[cx][cy] = 1
 
    
def dfs(n, lst):
    global answer
    if n == cctv_num:
        cnt = 0
        for i in lst:
            cnt += i.count(0)
        answer = min(answer, cnt)
        return 

    # n번째 cctv 정보
    cctv_type, cx, cy = cctv[n]
    for i in direction[cctv_type]:
        c_lst = copy.deepcopy(lst)
        working_cctv(i,cx,cy,c_lst)
        dfs(n+1, c_lst)


dfs(0,graph)
print(answer)


