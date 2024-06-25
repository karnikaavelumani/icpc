from collections import Counter

def solution(lines):
    freaky_map = Counter(lines)
    min_val = 1001
    res = []
    
    for key, value in freaky_map.items():
        if value == min_val:
            res.append(key)
        elif value < min_val:
            min_val = value
            res = [key]
    res.sort()
    for s in res:
        print(s)

lines = []

num_lines = int(input())
for i in range(num_lines):
    line = input()
    if line == "":
        break
    lines.append(line)
solution(lines)