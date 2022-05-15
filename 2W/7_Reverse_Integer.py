from collections import deque
from copy import copy

x = int(input())
r = deque(str(x)[::-1])
temp = copy(r)
if x == 0:
    print(0)
    exit(0)
for i in range(len(r)):
    if r[i] == '0':
        temp.popleft()
    else:
        break
if r[-1] == '-':
    temp.pop()
    temp.appendleft('-')

r = int(''.join(temp))
if r > 2**31 -1 or r < -2**31:
    print(0)
    exit(0)

print(r)

