class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_map_s = self.get_char_map(s)
        char_map_t = self.get_char_map(t)
        if (char_map_s == char_map_t):
            return True
        return False
        
    
    def get_char_map(self,s): 
        char_map = {}
        for ch in s:
            if ch not in char_map:
                char_map[ch] = 1
            else:
                char_map[ch] += 1
        return char_map
        