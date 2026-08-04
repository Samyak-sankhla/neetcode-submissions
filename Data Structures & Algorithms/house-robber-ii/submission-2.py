class Solution:
    def rob(self, nums: List[int]) -> int:
        prev=curr=0
        if len(nums) == 1:
            return nums[0]
        for num in nums[1:]:
            prev,curr=curr,max(prev+num,curr)
        prev=curr2=0
        for num in nums[:len(nums)-1]:
            prev,curr2=curr2,max(prev+num,curr2)
        return max(curr,curr2)