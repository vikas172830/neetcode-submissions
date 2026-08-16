class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         return True
        #     seen.add(num)
        # return False


        f = {}

        for num in nums:
            f[num] = f.get(num,0)+1

        for num in nums:
            if f[num] > 1:
                return True
        return False