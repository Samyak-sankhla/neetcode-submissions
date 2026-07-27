class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.reference=k
        self.data=nums[:]
        

    def add(self, val: int) -> int:
        self.data.append(val)
        self.data.sort()
        return self.data[-self.reference]
        
