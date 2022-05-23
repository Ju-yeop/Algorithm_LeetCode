from sys import stdin

nums = list(map(int, stdin.readline().strip().split()))
result = []
nums.sort()
for i in range(len(nums)):
    if i > 0 and nums[i] == nums[i - 1]:
        continue
    left = i + 1
    right = len(nums) - 1
    while left < right:
        total = nums[i] + nums[left] + nums[right]
        if total < 0:
            left += 1
        elif total > 0:
            right -= 1
        else:
            temp = [nums[i], nums[left], nums[right]]
            result.append(temp)
            left += 1
            right -= 1

temp = set(tuple(sorted(l)) for l in result)
print(list(list(item) for item in temp))