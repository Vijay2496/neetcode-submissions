class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if(len(nums)==1):
            return False
    
        z=len(nums)
        for read in range(z-1):
            if(nums[read] in nums[read+1:]):
                return True
                break
            else:
                continue
        return False



        