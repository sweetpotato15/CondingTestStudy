import sys
input = sys.stdin.readline
from math import ceil, floor
A, B = map(int, input().split())

b = floor(B**(1/2))

# a이상 b이하 소수개수 출력 - 소수의 제곱수 이므로 중복이 없음
prime = [True] * (b+1)
prime[0], prime[1] = False, False
for i in range(2, int(b**(1/2))+1):
    for j in range(2, b//i+1):
        if prime[i*j]:
            prime[i*j] = False

prime = [i for i in range(b+1) if prime[i]]

ans = 0
for i in prime:
    for j in range(2, 87):
        if (A <= i**j <= B):
            ans += 1
        elif i**j > B:
            break

print(ans)
