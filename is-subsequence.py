class Solution:
    def isSubsequence(self, s, t):
        
        s_index, t_index = 0, 0
        
        while s and t:
            if s[s_index] == t[t_index]:
                s = s[1:]
            
            t = t[1:]
            
        if not s:
            return True
        
        return False

s, t = "abc", "ahbgdc"
solution = Solution()
print(solution.isSubsequence(s, t))