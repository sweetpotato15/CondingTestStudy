# 백준 내리막길 1520

'''
- 내리막길만을 이용하여 출발지에서 도착지까지 가는 경우의 수
- dfs 이용해서 자기보다 작거나 같은 곳으로만 이동 -> 도착지에 갈 수 있으면 +1
    -> 시간초과
- + dp 
도착점에서 출발점으로 거꾸로 올라가는 dfs
'''
import sys
input = sys.stdin.readline

def dfs(ci,cj):
    if dp[ci][cj] == -1: # 아직 계산 안 된 경우(첫 방문)
        # 네 방향 (높은 곳에서 낮은 곳 방문시 경로수 누적)
        dp[ci][cj]=0
        for di, dj in ((-1,0),(1,0),(0,1),(0,-1)):
            pi,pj = ci+di, cj+dj # 이전 좌표 계산
            if height[pi][pj] > height[ci][cj]:
                dp[ci][cj] += dfs(pi,pj) # 네 방향 경로수 누적
    return dp[ci][cj]

N,M = map(int, input().split())
# 범위 체크를 생략하기 위해서 0으로 둘러싸기
height = [[0]*(M+2)] + [[0]+list(map(int, input().split()))+[0] for _ in range(N)] + [[0]*(M+2)] 

# dp테이블 생성 및 초기값 설정
dp = [[-1] * (M+2) for _ in range(N+2)]
dp[1][1] = 1

print(dfs(N,M))



'''
18 18
36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19
35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18
34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17
33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16
32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14
30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13
29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12
28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11
27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10
26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9
25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8
24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7
23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6
22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5
21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4
20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3
19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 10000
'''


