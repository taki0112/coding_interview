from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_nums = Counter(nums)
        most_nums = count_nums.most_common(k)

        x = []

        for n in most_nums:
            x.append(n[0])

        return x