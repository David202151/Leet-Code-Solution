class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0 
        for i in range(len(s)):
            seen = set()
            contador = 0 
            for j in range(i, len(s)):
                if s[j] in seen:
                    break
                contador += 1
                seen.add(s[j])
                max_len = max(max_len, contador)
        return(max_len)
                    
        
sol = Solution()
sol.lengthOfLongestSubstring('abcabcbb')