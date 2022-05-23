num = int(input())
result = ''
if num // 1000 > 0:
    f = num // 1000
    num -= f * 1000
    result += (f * 'M')
if num // 100 == 9:
    num -= 900
    result += "CM"
elif num // 100 == 4:
    num -= 400
    result += "CD"
elif num // 500 == 1:
    num -= 500
    result += "D"
    if num // 100 > 0:
        h = num // 100
        num -= h * 100
        result += (h*'C')
elif num // 100 > 0:
    h = num // 100
    num -= h * 100
    result += (h*'C')

if num // 10 == 9:
    num -= 90
    result += "XC"
elif num // 10 == 4:
    num -= 40
    result += "XL"
elif num // 50 == 1:
    num -= 50
    result += "L"
    if num // 10 > 0:
        t = num // 10
        num -= t * 10
        result += (t*'X')
elif num // 10 > 0:
    h = num // 10
    num -= h * 10
    result += (h*'X')

if num == 9:
    result += "IX"
elif num == 4:
    result += "IV"
elif num // 5 == 1:
    num -= 5
    result += "V"
    if num > 0:
        t = num
        result += (t*'I')
elif num > 0:
    h = num
    result += (h*'I')

print(result)