class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canship(capacity):
            finaldays=1
            curr_load=0
            for w in weights:
                if curr_load+w > capacity:
                    finaldays+=1
                    curr_load=0
                curr_load=curr_load+w
            return finaldays <= days
        left=max(weights)
        right=sum(weights)
        while left < right:
            mid = left + (right-left)//2
            if canship(mid):
                right=mid
            else:
                left=mid+1
        return left


            
            
        