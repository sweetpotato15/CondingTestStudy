import sys
input = sys.stdin.readline

N = int(input())
score = list(map(int, input().split()))

max_score = max(score)
score = [x*100/max_score for x in score]
print(sum(score)/len(score))