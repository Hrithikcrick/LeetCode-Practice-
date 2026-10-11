
from collections import defaultdict
from typing import List

class Solution:
    def countStableSubarrays(self, capacity: List[int]) -> int:

        n = len(capacity)

   
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + capacity[i]

    
        freq = defaultdict(int)
        ans = 0

        for right in range(2, n):

          
            left = right - 2

            freq[(capacity[left], prefix[left + 1])] += 1

           
            need = (
                capacity[right],
                prefix[right] - capacity[right]
            )

           
            ans += freq[need]

        return ans
