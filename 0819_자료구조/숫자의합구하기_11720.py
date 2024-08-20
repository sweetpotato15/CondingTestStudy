import sys
input = sys.stdin.readline

N = int(input())
num = list(input().strip())
num = [int(x) for x in num]
print(sum(num))
