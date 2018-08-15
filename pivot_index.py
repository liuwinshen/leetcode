import pdb

def pivot_index(nums):
    pdb.set_trace()
    if nums[0] == sum(nums[2:]):
        return 0

    for i in range(0, len(nums)-1):
        if sum(nums[0:i+1]) == sum(nums[i+2:]):
            return i+1
    return -1

print(pivot_index([-1,-1,-1,-1,0,1]))
