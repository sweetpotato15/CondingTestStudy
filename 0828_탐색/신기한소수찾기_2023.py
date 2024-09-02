# n=8 이므로 완전탐색 가능

def is_prime(x):
    for i in range(2, int(x**(1/2))+1):
        if x % i == 0:
            return False
    return True

def dfs(x, digit):
    if digit == N:
        print(x)
        return 
    for i in [1,3,5,7,9]:
        next_value = int(str(x)+str(i))
        if is_prime(next_value):
            dfs(next_value, digit+1)
    
N = int(input())
for i in [2,3,5,7]:
    dfs(i, 1)