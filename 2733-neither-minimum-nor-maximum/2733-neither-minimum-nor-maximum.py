class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        maximum = max(nums)
        minimum = min(nums)
        
        for n in nums:
            if n != maximum and n != minimum:
                return n
        return -1
        
        