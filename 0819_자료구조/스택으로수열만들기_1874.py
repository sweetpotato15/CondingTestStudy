import sys
input = sys.stdin.readline

n = int(input())
command = [int(input()) for _ in range(n)]

ans = ''
stack = []
num = 1 # stack에 이제 들어갈 값 (아직 안들어감)
result = True

for i in range(n):
    target = command[i]
    if target >= num: # target이 더 크면 더 만큼 append
        while target >= num:
            stack.append(num)
            num += 1
            ans += '+'
        stack.pop()
        ans += '-'

    else: # target이 이제 들어갈 값보다 작은 경우
        value = stack.pop()
        if value > target:
            print('NO')
            exit()
        else:
            ans += '-'

for i in ans:
    print(i, end='\n')

 

'''
<기존 풀이방법 >

command : 2 3 4 1 5

완성 array : [1 2 3 4 5]

now_index=0 -> 1 -> 0, ans = ++- array:[1 3 4 5]
now_index=0 -> 1 -> 0, ans = ++-+- array:[1 4 5]
now_index=0 -> 1 -> 0, ans = ++-+-+- array:[1 5]
now_index=0 -> 1 -> 0, ans = ++-+-+-- array:[5]
now_index=0, ans = ++-+-+--- array:[]  <- 문제 발생 (5는 append 하지 않았는데 기존에 있다고 판단하여 + 를 해주지 않음)

문제점1)
array 는 모든 숫자가 이미 담겨있기 때문에 실제 stack에 append 된 것인지 아직 안된것인지 구별할 방법이 없음
(자동으로 index 가 하나씩 땡겨지기 때문에)

문제점2)
1)에 이어서 4는 원래 append 가 안된 값인데 구별 불가라 append 됐다고 생각하고 pop을 해버림..
'''

'''
import sys
input = sys.stdin.readline

n = int(input()) # 수열 개수
command = [int(input()) for _ in range(n)] # 순서대로 나와야할 값
ans = '+'

array = list(range(1, n+1)) # 완성 array [1,2,3,4,..,8]
now_index = 0 # 현재 index 값 

for i in range(n): 
    if array[now_index] <= command[i]: #array[0] : 1, command[0] :4
        next_index = array.index(command[i])
        ans += '+'*(next_index-now_index)
        now_index = next_index
    elif array[now_index] > command[i]: 
        print('NO')
        exit()
    array.pop(now_index)
    ans += '-'
    now_index = max(0, now_index-1)

print(ans)
'''