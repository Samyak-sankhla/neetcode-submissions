class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        to_replace=1
        for i in range(1, len(nums)):
            if nums[i] != nums [i-1]:
                nums[to_replace] = nums[i]
                to_replace+=1
        return to_replace