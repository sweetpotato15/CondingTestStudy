'''
출발지에서 정상까지 가는 길을 최소로 만들면 편도만 구하면 된다. (왕복 고려x)
-> 힙 자료구조 이용

'''
import heapq
def dijkstra(n,start):
    global distance
    distance = [0]*(n+1)
    q = []
    heapq.heappush(q, (0, start)) # (비용, 지점)
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] >= dist:
            continue
        for i in graph[now]:
            cost = max(cost, distance[i])
            if cost >= distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))


def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n+1)] # (도착지, 비용)
    for path in paths:
        i,j,w = path
        graph[i].append([j,w])
        graph[j].append([i,w])
    
    intensity = int(1e9)
    top = n+1
    for i in gates:
        result = dijkstra(n,i)
        for j in summits:
            if distance[j] <= intensity:
                intensity = distance[i]
                top = min(top, j)
                
    answer = [intensity, top]
    return answer
