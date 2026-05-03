class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # We know the max freq is len(nums)
        count = Counter(nums)
        freq = [[] for i in range(len(nums)+1)]
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        res = []
        for i in range(len(nums), 0, -1):
            for val in freq[i]:
                res.append(val)
                if len(res) == k:
                    return res
