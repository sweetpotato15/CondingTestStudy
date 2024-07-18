'''
LRU 알고리즘 : 가장 오랫동안 참조되지 않은 페이지를 교체하는 기법
- cache hit : cpu가 참조하고자 하는 메모리가 캐시에 존재하고 있을 경우
    -> 원래 위치 node 삭제하고 head 바로 뒤에 원소 추가
- cache miss : cpu가 참조하고자 하는 메모리가 캐시에 존재하지 않을 경우

'''
from collections import deque

def solution(cacheSize, cities):
    cities = [x.lower() for x in cities]
    cities = deque(cities)
    cache = deque()
    # cache = collections.deque(maxlen=cacheSize)
    ans = 0

    while cities:
        now = cities.popleft()
        if now in cache:
            ans += 1
            cache.remove(now)
        else:
            ans += 5
        cache.appendleft(now)
        cache = deque(list(cache)[:cacheSize])
        
    return ans

print(solution(3,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(3,["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))