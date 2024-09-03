M, N = map(int, input().split())

prime = [True] * (N+1)
prime[0], prime[1] = False, False

for i in range(2, int(N**(1/2))+1):
    for j in range(2, N//i+1):
        if prime[i*j]:
            prime[i*j] = False
    
for i in range(M, N+1):
    if prime[i]:
        print(i)