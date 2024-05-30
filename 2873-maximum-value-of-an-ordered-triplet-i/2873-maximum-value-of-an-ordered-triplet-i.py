class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        max_value = 0
        for k in range(n-1, 1, -1):
            for i in range(k):
                for j in range(i+1, k):
                    if i < j and j < k:
                        temp = (nums[i] - nums[j]) * nums[k]
                        if temp > max_value:
                            max_value = temp
        return max_value
            
            
            
        