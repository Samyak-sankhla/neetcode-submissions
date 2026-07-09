class Solution:
    def validPalindrome(self, s: str) -> bool:
        left=0
        right=len(s)-1
        while left < right:
            if s[left] != s[right]:
                skip_l = s[left+1:right+1]
                skip_r = s[left:right]
                return skip_l == skip_l[::-1] or skip_r == skip_r[::-1]
            left+=1
            right-=1
        return True