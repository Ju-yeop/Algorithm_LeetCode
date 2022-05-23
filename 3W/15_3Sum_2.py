from sys import stdin

def dfs(idx, list):
    if len(list) == 3:
        if sum(list) == 0:
            answer.append(list[:])
            return

    for i in range(idx, len(ls)):
        dfs(i+1,list+[ls[i]])

ls = list(map(int, stdin.readline().strip().split()))
answer = []
dfs(0, [])

temp = set(tuple(sorted(l)) for l in answer)
print(list(list(item) for item in temp))