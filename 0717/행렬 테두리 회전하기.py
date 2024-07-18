from collections import deque
def rotate_mat(lst, query):
    x1,y1,x2,y2 = query
    before = deque()
    for i in range(y1,y2):
        before.append(lst[x1][i])
    for i in range(x1,x2):
        before.append(lst[i][y2])
    for i in range(y2,y1,-1):
        before.append(lst[x2][i])
    for i in range(x2,x1,-1):
        before.append(lst[i][y1])

    value = min(before)
    before.rotate(1)

    for i in range(y1,y2):
        lst[x1][i] = before.popleft()
    for i in range(x1,x2):
        lst[i][y2] = before.popleft()
    for i in range(y2,y1,-1):
        lst[x2][i] = before.popleft()
    for i in range(x2,x1,-1):
        lst[i][y1] = before.popleft()
    return value

def solution(rows, columns, queries):
    graph = [[0]*(columns+1)] + [[] for _ in range(rows)]
    ans = []
    
    for i in range(rows):
        graph[i+1] = [0] + list(range(i*columns+1,(i+1)*columns+1))
    
    for i in queries:
        ans.append(rotate_mat(graph, i))
    
    return ans

answer = solution(3,3,[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]])
print(answer)