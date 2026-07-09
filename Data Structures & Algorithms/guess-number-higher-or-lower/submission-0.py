# The guess API is already defined for you.
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        beg, end = 1, n
        while beg <= end:
            mid = beg + (end - beg) // 2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == 1:
                beg = mid + 1
            else:
                end = mid - 1
        return 0  