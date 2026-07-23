class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        def backtrack(remain, idx, path):
            if remain==0:
                ans.append(path.copy())
                return
            if idx==len(candidates) or remain<0:
                return
            path.append(candidates[idx]) 
            backtrack(remain-candidates[idx],idx,path)
            path.pop()
            backtrack(remain,idx+1,path)
        backtrack(target,0,[])
        return ans         