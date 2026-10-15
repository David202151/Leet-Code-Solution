class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        j = 0
        palindrome = ""
        len_s = len(s)
        if len_s < 2:
            return s
        else: 
            for i in range (len_s): 
                for j in range (len_s + 1): 
                    if s[i:j] == s[i:j][::-1]:
                        if len(s[i:j]) > len(palindrome):
                            palindrome = s[i:j]
            print(palindrome)
            return palindrome

Solution().longestPalindrome("cbbd")
                    
