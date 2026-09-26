class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen={}
         
        for i, num in enumerate(nums):
            partner=target-nums[i]
            if partner in seen:
                return [seen[partner],i]
            seen[num]=i  
        