'''
가로 세로 별 취할 수 있는 동작이 8개임 
- 상하좌우, 축 회전 4가지

로봇이 차지하는 칸이 2칸임 
'''
from collections import deque

def solution(board):
    n = len(board)
    # 범위 생각 안하기 위해서 테두리에 벽 생성
    board = [[1]*(n+2)] + [[1]+x+[1] for x in board] + [[1]*(n+2)]
    
    q = deque([[(1,1),(1,2),0]]) # 현재 로봇 좌표와 거리 
    ch_set = set([((1,1),(1,2))]) # 방문한 적이 있는지 확인하기 위한 set
    while q :
        s1, s2, dis = q.popleft()
        if s1 == (n,n) or s2 == (n,n) :
            return dis
        
        possible = []
        # 상하좌우 이동
        for (di,dj) in [(-1,0),(0,1),(1,0),(0,-1)]:
            s1_i = s1[0] + di
            s1_j = s1[1] + dj
            s2_i = s2[0] + di
            s2_j = s2[1] + dj
            
            if board[s1_i][s1_j] == 0 and board[s2_i][s2_j] ==0:
                possible.append(((s1_i,s1_j),(s2_i,s2_j)))
        
        # 수평 -> 수직 (4가지 경우 존재)
        if s1[0] == s2[0]:
            # 위로 90도 (위의 블록2개가 모두 0) 아래로 90도(아래 블록 2개가 모두 0)
            for i in [1,-1]:
                if board[s1[0]+i][s1[1]] == 0 and board[s2[0]+i][s2[1]] == 0:
                    possible.append((s1, (s1[0]+i,s1[1])))
                    possible.append((s2, (s2[0]+i,s2[1])))
                    
        # 수직 -> 수평 (4가지 경우 존재)            
        else:
            for i in [1,-1]:
                if board[s1[0]][s1[1]+i] == 0 and board[s2[0]][s2[1]+i] == 0:
                    possible.append((s1, (s1[0],s1[1]+i)))
                    possible.append((s2, (s2[0],s2[1]+i)))
                    
        for p in possible:
            if p not in ch_set:
                q.append((*p, dis+1))
                ch_set.add(p)
 