import sys
input = sys.stdin.readline

string = input().strip().split('-')
string = [x.split('+') for x in string]
string = [list(map(int, x)) for x in string]
string = [sum(x) for x in string]
print(string[0] - sum(string[1:]))