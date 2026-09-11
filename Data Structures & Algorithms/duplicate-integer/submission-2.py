class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s=''
        test= True
        i=0
        while i != len(nums) and test == True:
            if ' '+str(nums[i])+' ' in s:
                test= False
            else:
                s+=' '+str(nums[i])+' '
                i=i+1
        return not(test)
