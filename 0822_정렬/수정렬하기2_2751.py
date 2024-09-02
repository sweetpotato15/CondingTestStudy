import sys
input = sys.stdin.readline

n = int(input())
number = sorted([int(input()) for _ in range(n)])
print(*number, sep='\n')