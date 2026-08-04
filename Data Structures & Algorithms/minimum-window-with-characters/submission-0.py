from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t) > len(s):
            return ""
        # dictionaries for storing needed char count and current window char count
        need=Counter(t)
        window=defaultdict(int)
        # variables to keep that of lengths
        req=len(need)
        formed=0
        # variables for best index and best size
        best_size=float("inf")
        best_start=0
        # variables for traversing
        left,right=0,0
        for right in range(len(s)):
            char = s[right]
            window[char]+=1
            if char in need and window[char] == need[char]:
                formed+=1
            while formed==req:
                curr_size = right-left+1
                if curr_size < best_size:
                    best_size=curr_size
                    best_start=left
                left_char = s[left]
                window[left_char]-=1
                if left_char in need and window[left_char] < need[left_char]:
                    formed-=1
                left+=1
        if best_size == float("inf"):
            return ""
        return s[best_start:best_start+best_size]




        
        