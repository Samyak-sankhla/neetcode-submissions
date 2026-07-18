class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged=''
        i=0
        while i < len(word1) and i < len(word2):
            merged = merged + word1[i]
            merged = merged + word2[i]
            i+=1
        if i > len(word1)-1 and i < len(word2):
            merged = merged + word2[i:]
        elif i > len(word2)-1 and i < len(word1):
            merged = merged + word1[i:]
        return merged