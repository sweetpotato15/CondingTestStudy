'''
트리 깊이가 n이면 노드 수가 2^n-1임 
1 3 7 15 ...

'''
from bisect import bisect_right

def can_binary(s):

    if len(s) == 1:
        return 1
    mid = len(s) // 2
    if s[mid] == '0' and '1' in s:
        return 0
    left = can_binary(s[:mid])
    right = can_binary(s[mid+1:])
    return left*right

def solution(numbers):
    ans = []
    nodes = [2**x-1 for x in range(1,46)]
    for i in numbers:
        string = bin(i)[2:]
        c = 1
        if len(string) in nodes:
            node = len(string)
        else:
            node = nodes[bisect_right(nodes, len(string))]
        string = '0'*(node-len(string)) + string
        res = can_binary(string)
        ans.append(res)
    return ans

print(solution([7, 42, 5]))
print(solution([ 95]))
