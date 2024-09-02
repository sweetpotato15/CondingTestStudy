import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right

_ = int(input())
A = sorted(list(map(int, input().split())))

_ = int(input())
M = list(map(int, input().split()))

for value in M:
    left = bisect_left(A, value)
    right = bisect_right(A, value)

    if left == right:
        print(0)
    else:
        print(1)