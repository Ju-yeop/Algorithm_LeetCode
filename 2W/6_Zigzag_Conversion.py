s = list(input())
row = int(input())
ls = [[] for _ in range(1000)]
temp = 0
judge = True   # 인덱스 값을 +하냐 -하냐를 판단
for i in range(len(s)):
    ls[temp].append(s[i])
    if temp - 1 == -1:
        judge = True
    elif temp + 1 == row:
        judge = False


    if judge is True:
        temp += 1
    else:
        temp -= 1

for v in range(1000):
    if len(ls[v]) == 0:
        break
    print(''.join(ls[v]), end='')
