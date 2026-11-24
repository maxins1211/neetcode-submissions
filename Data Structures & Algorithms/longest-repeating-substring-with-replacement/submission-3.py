class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = {}
        left = right = 0
        max_freq = max_len = 0
        while right < len(s):
            freqs[s[right]] = freqs.get(s[right], 0) + 1
            max_freq = max(max_freq,freqs[s[right]])
            num_chars_to_replace = right - left + 1 - max_freq
            if num_chars_to_replace > k:
                freqs[s[left]] -= 1
                left += 1
            max_len = right - left + 1
            right += 1
        return max_len