class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        def backtrack(i,ele):
            if ele not in res:
                res.append(ele.copy())
            if i > len(nums)-1:
                return
            ele.append(nums[i])
            backtrack(i+1,ele)
            ele.pop()
            backtrack(i+1,ele)
        backtrack(0,[])
        return res
        