class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_map = defaultdict(list)
        for word in strs:
            ch_arr = [0] * 26
            for ch in word:
                ch_arr[ord(ch) - ord('a')] += 1
            anagrams_map[tuple(ch_arr)].append(word)
        return list(anagrams_map.values())