from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)

        if window_size > len(s2):
            return False

        s1_count = Counter(s1)
        window_count = Counter(s2[:window_size])

        if s1_count == window_count:
            return True

        for right in range(window_size, len(s2)):
            entering_char = s2[right]
            leaving_char = s2[right - window_size]

            window_count[entering_char] += 1
            window_count[leaving_char] -= 1

            if window_count[leaving_char] == 0:
                del window_count[leaving_char]

            if window_count == s1_count:
                return True

        return False