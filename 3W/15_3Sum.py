from itertools import combinations
from sys import stdin

nums = list(map(int, stdin.readline().strip().split()))
candidates = list(combinations(nums, 3))
result = []
for i in range(len(candidates)):
    if sum(candidates[i]) == 0:
        result.append(list(candidates[i]))

temp = set(tuple(sorted(l)) for l in result)
print(list(list(item) for item in temp))