class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        combined = 0

        for num in nums:
            combined |= num

        return combined << (len(nums) - 1)