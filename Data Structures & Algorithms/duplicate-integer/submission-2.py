class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        if sorted(nums) == sorted(set(nums)):
            return False
        else: 
            return True



         