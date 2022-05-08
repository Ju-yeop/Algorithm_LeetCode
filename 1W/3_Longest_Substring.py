s = input()

temp = []
maxi = 0
sub_max = 0
if len(s) <= 1:
    print(len(s))
else:
    for i in range(len(s)):
        if s[i] not in temp:
            temp.append(s[i])
            sub_max += 1
        else:
            if maxi < sub_max:
                maxi = sub_max
                sub_max = 1
                temp.clear()
                temp.append(s[i])
        if i == len(s)-1 and maxi < sub_max:
            maxi = sub_max
    print(maxi)

# ex) dvdf와 같은 경우 에러

