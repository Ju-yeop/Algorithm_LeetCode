from sys import stdin

ls = list(map(int, stdin.readline().strip().split()))
result = 0
for i in range(len(ls)):
    for j in range(i+1, len(ls)):
        temp = (j-i) * min(ls[i], ls[j])
        if temp > result:
            result = temp

print(result)