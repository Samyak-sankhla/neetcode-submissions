class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        n=len(nums)
        picked=[False]*n
        def dfs(comb):
            if len(comb) == n and comb not in res:
                res.append(comb[:])
            for i in range(n):
                if not picked[i]:
                    picked[i]=True
                    comb.append(nums[i])
                    dfs(comb)
                    comb.pop()
                    picked[i]=False
        dfs([])
        return res
        