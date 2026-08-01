class Solution:
    def findMin(self, nums: List[int]) -> int:
        import heapq
        heapq.heapify(nums)
        return heapq.heappop(nums)

        