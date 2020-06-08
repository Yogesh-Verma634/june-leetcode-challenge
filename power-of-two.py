class Solution:
    #n: int
    def isPowerOfTwo(self, n):
        
        if n == 0:
            return False
        return n & (n-1) == 0 

solution = Solution()
print(solution.isPowerOfTwo(5))
print(solution.isPowerOfTwo(10))
print(solution.isPowerOfTwo(1))
print(solution.isPowerOfTwo(0))