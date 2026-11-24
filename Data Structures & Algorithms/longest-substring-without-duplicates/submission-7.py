class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        left = right = 0
        max_count = current_count = 0
        substr_map = {}
        while right < length:
            if s[right] not in substr_map:
                substr_map[s[right]] = 1
                right += 1
                current_count += 1
            else:
                del substr_map[s[left]]
                left += 1
                current_count -= 1
            if max_count < current_count:
                max_count = current_count
        return max_count