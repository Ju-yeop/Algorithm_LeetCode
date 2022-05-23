from sys import stdin

height = list(map(int, stdin.readline().strip().split()))
result = 0
left = 0
right = len(height) - 1
for _ in range(len(height)):
    result = max(result, min(height[left], height[right]) * (right - left))
    if height[left] <= height[right]:
        left += 1
    else:
        right -= 1

print(result)
