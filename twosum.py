import itertools

def twoSum(nums, target):
    i = 0
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

print(twoSum([2,5,5,11], 10))
print(twoSum([3,3,5,11], 6))
