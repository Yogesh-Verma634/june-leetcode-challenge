import random
class Solution:
    #w: List[int]
    def __init__(self, w):
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        
        target = self.total_sum * random.random()
        start, end = 0, len(self.prefix_sums) - 1
        
        while start < end:
            mid = start + ((end - start) // 2)
            
            if target > self.prefix_sums[mid]:
                start = mid + 1
            else:
                end = mid
        return start
                    
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()