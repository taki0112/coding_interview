from collections import defaultdict

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x = defaultdict(int)

        for n in nums:
            x[n] += 1

        for k, v in x.items():
            if v == 1:
                return k