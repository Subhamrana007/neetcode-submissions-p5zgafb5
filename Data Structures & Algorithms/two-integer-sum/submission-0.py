class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        emty_dict = dict()
        for i ,n in enumerate (nums):
            diff = target - n
            if diff in emty_dict:
                return (emty_dict[diff],i)

           
            emty_dict[n]= i



        