import sys
input = sys.stdin.readline

N = int(input())
array = [list(map(int, input().split())) for _ in range(N)]
array = sorted(array, key=lambda x: (x[1], x[0]))

start, end = array[0]
count = 1
for i in range(1,N):
    if end <= array[i][0]:
        count += 1
        end = array[i][1]
print(count)