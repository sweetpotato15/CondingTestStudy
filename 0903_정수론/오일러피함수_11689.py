# 오일러 피함수, n이하 자연수 중에서 n과 서로소인 개수

n = int(input())
answer = n

for i in range(2, int(n**(1/2))+1):
    if n % i == 0: # 약수이면
        answer = answer - answer//i
        while n % i ==0:
            n = n // i # 해당 소인수 지우기 

if n > 1:
    answer -= answer//n
print(answer)