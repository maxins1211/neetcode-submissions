from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        freqs = set()
        freq_num_map = defaultdict(list)
        num_freq_map = defaultdict(int)
        for num in nums:
            num_freq_map[num] += 1
        
        for key in num_freq_map:
            freq = num_freq_map[key]
            if freq not in freqs:
                freqs.add(freq)
            freq_num_map[freq].append(key)

        sorted_freqs = sorted(freqs)
        for i in range(len(sorted_freqs) - 1,-1,-1):
            result = result + freq_num_map[sorted_freqs[i]]
            if len(result) >= k:
                break
        return result
