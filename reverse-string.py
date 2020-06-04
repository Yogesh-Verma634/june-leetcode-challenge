class Solution:
    #s: List[str]
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        start, end = 0, len(s)-1
        while start<end:
            s[start], s[end] = s[end], s[start]
            
            start += 1
            end -= 1
        return s
string = ['h', 'e', 'l', 'l', 'o']
solution = Solution()
print(solution.reverseString(string))