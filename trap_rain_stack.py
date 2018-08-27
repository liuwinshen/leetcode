def trap(height):
	if len(height) <3:
		return 0

	trapped = 0
	bars = []

	for i in range(len(height)):
		if not bars or height[i] <= height[bars[-1]]:
			bars.append(i)
			continue
		while height[i] > height[bars[-1]]:
			top = bars.pop()
			if not bars:
				bars.append(i)
				continue
			distance = i - bars[-1] - 1
			trapped_height = min(height[bars[-1]], height[i]) - height[top]
			trapped += distance * trapped_height
		bars.append(i)
	return trapped

print(trap([0,1,0,2,1,0,1,3,2,1,2,1])) # 6
print(trap([4,2,3])) # 1

# Time complexity: O(n)
# Space complexity: O(n)
