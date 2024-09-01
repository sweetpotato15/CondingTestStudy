import sys
input = sys.stdin.readline

N, K = map(int, input().split())
array = [int(input()) for _ in range(N)][::-1]

ans = 0
for i in range(N):
    if K == 0:
        break
    if K//array[i] > 0:
        ans += K//array[i]
        K %= array[i]
print(ans)
                                    

