class Solution:
    def isPalindrome(self, s: str) -> bool:
        mod_str=""
        for i in s:
            if i.isalnum():
                mod_str=mod_str+i
        mod_str=mod_str.lower()
        if mod_str[:] == mod_str[::-1]:
            return True
        return False        