s= input()
if len(s) <= 1:
    print(s)
i, l= 0, 0
for j in range(len(s)):
    if s[j-l: j+1] == s[j-l: j+1][::-1]:
        i, l = j-l, l+1
        print(s[i: i+l])
    elif j-l > 0 and s[j-l-1: j+1] == s[j-l-1: j+1][::-1]:
        i, l = j-l-1, l+2
        print(s[i: i+l])

""" 길이가 L인 palindrome에 문자 하나를 추가했을 때 만들어지는 palindrome을 생각해보면, 길이가 L+1 또는 L+2 이다.
그런데 내가 이미 알고있는 palindrome의 길이가 L이라면, 길이가 L이하인 palindrome의 존재는 체크할 필요도 없다.
각 문자 s[i]에 대해 그 문자를 마지막 문자로 하는 길이 L+1 또는 L+2 인 palindrome이 있는지만 탐색하면 된다."""