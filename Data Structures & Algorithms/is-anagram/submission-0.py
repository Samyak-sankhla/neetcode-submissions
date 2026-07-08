class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        countS = {}
        countT = {}

        for i in s:
            if i in countS:
                countS[i] += 1
            else:
                countS[i] = 1
        for j in t:
            if j in countT:
                countT[j] += 1
            else:
                countT[j] = 1

        for k in s:
            if k in t:
                if countS[k] != countT[k]:
                    return False
            else:
                return False

        return True
            
            

        