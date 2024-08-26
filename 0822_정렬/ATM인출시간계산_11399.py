N = int(input())
array = sorted(list(map(int, input().split())))

for i in range(1,N):
    array[i] += array[i-1]
print(sum(array))