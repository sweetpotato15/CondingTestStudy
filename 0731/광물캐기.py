from collections import Counter

def solution(picks, minerals):
    answer = 0
    n_picks = sum(picks)
    mineral = []
    for i in range(0,len(minerals),5):
        counter = Counter(minerals[i:i+5])
        mineral.append([counter['diamond'], counter['iron'],counter['stone']])
    mineral = sorted(mineral[:min(n_picks,len(mineral))], reverse = True) # 다이아가 많은 순으로

    for _ in range(picks[0]): # 다이아 곡괭이
        if not mineral:
            break
        now = mineral.pop(0)
        answer += sum(now)
    for _ in range(picks[1]) : # 철 곡괭이
        if not mineral:
            break
        now = mineral.pop(0)
        answer += now[0] * 5 + now[1] + now[2]
    for _ in range(picks[2]): # 돌 곡괭이
        if not mineral:
            break
        now = mineral.pop(0)
        answer += now[0] * 25 + now[1] * 5 + now[2]

    return answer