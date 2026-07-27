import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x,y in points:
            distance = -(x*x + y*y) #taking negative, as in python it is min-heap, need to remove largest positive, which will be least value in negative
            if len(heap) == k:
                heapq.heappushpop(heap, (distance,x,y))
            else:
                heapq.heappush(heap,(distance,x,y))
        return [(x,y) for (distance,x,y) in heap]