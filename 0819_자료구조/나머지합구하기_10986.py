'''
연속된 부분의 합이 M으로 나누어떨어지는 구간의 개수
-> 각 수를 나머지로 변환 후 누적합

1) i=j 인 경우 : 0 count
2) i<j 인 경우 : 나머지가 같은 수 count -> 조합 개수
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
array = list(map(int, input().split()))

array = [0] + [x%M for x in array]
sum_array = [0] * (N+1)

for i in range(1, N+1):
    sum_array[i] = (sum_array[i-1] + array[i]) % M
sum_array = sum_array[1:]

## sol1) 나머지 같은 수 count 하기 -> 시간복잡도 O(N*M) 최대 10^9
ans = sum_array.count(0)
for i in range(M):
    value = sum_array.count(i)
    ans += value*(value-1)//2
print(ans)

## sol2) 나머지에 해당하는 index의 값 += 1 -> 시간복잡도 O(N+M) 최대 10^6
C = [0] * (M)
for i in sum_array:
    C[i] += 1

ans = C[0]
for i in range(M):
    ans += C[i] * (C[i]-1) // 2
print(ans)