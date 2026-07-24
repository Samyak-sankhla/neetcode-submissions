class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        if len(nums) <= 1:
            return [nums]
        pick = [False]*len(nums)
        def backpermute(comb):
            if len(comb) == len(nums):
                res.append(comb[:])
            for i in range(len(nums)):
                if not pick[i]:
                    comb.append(nums[i])
                    pick[i]=True
                    backpermute(comb)
                    comb.pop()
                    pick[i]=False
        backpermute([])
        return res

        
        