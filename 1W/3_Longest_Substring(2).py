s = input()

maxi = 0
for i in range(len(s)):
    temp = ""
    sub_max = 0
    for j in range(i, len(s)):
        if s[j] in temp:
            if sub_max > maxi:
                maxi = sub_max
            break
        temp += s[j]
        sub_max += 1
        if j == len(s)-1:
            if sub_max > maxi:
                maxi = sub_max
            break


print(maxi)

