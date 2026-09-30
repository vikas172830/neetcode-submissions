from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        f = {}
        for i in nums:
            f[i] = f.get(i,0)+1

        sorted_freq = sorted(
            f.items(),
            key=lambda x: x[1],
            reverse=True
        )

        # Step 3: Return the top k numbers
        return [num for num, freq in sorted_freq[:k]]