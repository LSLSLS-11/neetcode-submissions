class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h={}
        for i,j in enumerate(nums):
            h[j]=i
        for i in range(len(nums)):
            if (target - nums[i]) in h and i != h[target - nums[i]]:
                return [i,h[target - nums[i]]]
        