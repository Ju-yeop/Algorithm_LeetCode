from collections import deque

x = input()
r = deque(x)
result = []
for i in range(len(r)):
    if len(result) == 0 and r[i] == ' ':
        continue
    elif r[i] == '':
        break
    elif len(result) == 0:
        if r[i] == '-' or r[i] == '+' or 48 <= ord(r[i]) <= 57:
            result.append(r[i])
        else:
            break
    elif 48 <= ord(r[i]) <= 57:
        result.append(r[i])
    else:
        break

if len(result) == 0:
    print(0)
    exit(0)
try:
    result = int(''.join(result))
    if result > 2 ** 31 - 1:
        result = 2 ** 31 - 1
    elif result < -2 ** 31:
        result = -2 ** 31
    print(result)
except:
    print(0)
