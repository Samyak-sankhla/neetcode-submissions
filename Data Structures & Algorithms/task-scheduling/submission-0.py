from collections import Counter
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequencies = Counter(tasks)

        max_frequency = max(frequencies.values())

        max_frequency_tasks = sum(
            1 for frequency in frequencies.values()
            if frequency == max_frequency
        )

        required_intervals = (
            (max_frequency - 1) * (n + 1)
            + max_frequency_tasks
        )

        return max(len(tasks), required_intervals)