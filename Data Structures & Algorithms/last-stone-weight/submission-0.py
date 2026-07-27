import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)
        while len(stones) > 1:
            ele1 = -(heapq.heappop(stones))
            ele2 = -(heapq.heappop(stones))
            diff = abs(ele1-ele2)
            heapq.heappush(stones,-diff)
        return -(stones[0])