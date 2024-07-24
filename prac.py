# import sys
# input = sys.stdin.readline

# N = int(input())
# tree_set = {}
# for _ in range(N):
#     string = input().strip().split(' ')
#     tree_set[string[0]] = string[1:]

# answer1, answer2, answer3 = '', '', ''
# def dfs1(v):
#     global answer1
#     if v != '.':
#         answer1 += v
#         for i in tree_set[v]:
#             dfs1(i)

# def dfs2(v):
#     global answer2
#     answer = ''
#     if v != '.':
#         answer2 += v
#         for i in tree_set[v]:
#             dfs2(i)
#         answer2 = v + answer2
#         # answer2 += answer[::-1]

# def dfs3(v):
#     global answer3
#     if v != '.':
#         for i in tree_set[v]:
#             dfs3(i)
#         answer3 += v
# # dfs1('A')
# # print(answer1)

# dfs2('A')
# print(answer2)

# # dfs3('A')
# # print(answer3)

a = {}
a[0] =1
a[2]=4
x,y = a.popitem()
print(x,y)
print(a.popitem())