class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        def backtrack(remain, idx, path):
            if remain == 0:
                ans.append(path.copy())
                return
            if idx == len(candidates) or remain < 0:
                return 
            path.append(candidates[idx])
            backtrack(remain-candidates[idx],idx+1,path)
            path.pop()
            next_idx=idx+1
            while (next_idx < len(candidates) and candidates[next_idx]==candidates[next_idx-1]):
                next_idx+=1
            backtrack(remain, next_idx, path)
        backtrack(target, 0, [])
        return ans





        