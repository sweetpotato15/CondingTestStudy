'''
changed = False
for i in range(N):
    changed = False
    for j in range(N-i-1):
        if A[j] > A[j+1]:
            changed = True
            A[j], A[j+1] = A[j+1], A[j]
    if changed == False:
        print(i+1)
        break
'''
# 순서변화가 없을때의 index 출력

import sys
input = sys.stdin.readline

N = int(input())
A = list(enumerate([int(input()) for _ in range(N)]))

sorted_A = sorted(A, key=lambda x:x[1])

ans = 0
for i in range(N):
    ans = max(ans, sorted_A[i][0]-i)
print(ans+1)

 