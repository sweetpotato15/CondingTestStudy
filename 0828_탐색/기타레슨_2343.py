import sys
input = sys.stdin.readline

N, M = map(int, input().split())
array = list(map(int, input().split()))

def cal_count(limit):
    ans = 0
    total = 0
    for i in range(N):
        total += array[i]
        if total == limit:
            ans += 1
            total = 0
        elif total > limit:
            ans += 1
            total = array[i]
    if total > 0:
        ans += 1
    return ans

# 블루레이의 값을 조정하면서 개수가 맞는지를 확임
start = max(array) # 블루레이 값의 최소
end = sum(array) # 블루레이 값의 최대

# 목표 : mid_count == M 이면서 mid_value 값이 최소
while start <= end:
    mid_value = (start+end)//2 # 블루레이 값 (최대 영상길이)
    mid_count = cal_count(mid_value) # 블루레이 개수
    if mid_count > M: # 개수가 많다 == 블루레이 값이 작다
        start = mid_value+1
    else: # 개수가 적거나 같다 == 블루레이 값이 크다
        end = mid_value-1
print(start)