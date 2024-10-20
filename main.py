from typing import List

def twoSum(nums: List[int], target: int) -> List[int]: # Your Codes
## Do not use input() or print() in your function
## Inputs (nums, target) will given as arguments and the output as ## return value
    ans = []
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                ans.append(i)
                ans.append(j)
    return ans