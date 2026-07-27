class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total=0
        best_max=curr_max=nums[0]
        best_min=curr_min=nums[0]
        for i,x in enumerate(nums):
            total+=x
            if i==0:
                continue
            curr_max=max(x,curr_max+x)
            best_max=max(best_max,curr_max)
            curr_min=min(x,curr_min+x)
            best_min=min(best_min,curr_min) #used for wrapping
        if best_max<0: #in case all elements are <0
            return best_max
        return max(best_max,total-best_min)
        