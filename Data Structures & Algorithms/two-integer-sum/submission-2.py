class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = 1
        List = []
        x = len(nums)
        for i in range(x):
            for j in range(i+1,x):
                if nums[i] + nums[j] == target:
                    List.append(i)
                    List.append(j)
                    return List
                j += 1
            i += 1
        

