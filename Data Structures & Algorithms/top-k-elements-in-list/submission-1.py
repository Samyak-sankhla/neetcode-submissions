class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result=[]
        freq={}
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
        result = list(freq.keys())
        return result[:k]

