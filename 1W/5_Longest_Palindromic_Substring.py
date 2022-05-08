s = input()
max_subs = []
for j in range(len(s)):
    temp = list(s[j:])
    length = len(temp)
    for v in range(length):
        if len(temp) > len(max_subs):
            if temp == temp[::-1]:
                max_subs = temp
                break
        temp.pop()

print(''.join(max_subs))

# O(n^3) 시간초과
