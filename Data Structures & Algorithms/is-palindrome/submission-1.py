class Solution:
    def isPalindrome(self, s: str) -> bool:
        mod_str=""
        for i in s:
            if i.isalnum():
                mod_str=mod_str+i
        mod_str=mod_str.lower()
        left=0
        right=len(mod_str)-1
        while left<=right:
            if mod_str[left]!=mod_str[right]:
                return False
            left+=1
            right-=1
        return True
        