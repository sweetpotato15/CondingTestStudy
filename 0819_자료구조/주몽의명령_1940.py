'''
2개의 합이 M이 되는 경우의 수
'''

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
array = sorted(list(map(int, input().split())))

start, end = 0, N-1
ans = 0

while start < end:
    value = array[start] + array[end]
    if value == M:
        ans += 1
        start += 1  # 정답인 경우 start+=1, end-=1 하면 더 효율적임. 
                    # 왜냐면 start+=1 만 하면 어짜피 value > M이 되기 때문에 다음 for문에서 end-=1가 됨
    elif value > M:
        end -=1
    else:
        start += 1

print(ans)
