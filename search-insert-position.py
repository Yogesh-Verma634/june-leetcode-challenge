class Solution:
    # nums: List[int]
    def searchInsert(self, nums, target):
        
        if len(nums) == 1:
            if target > nums[0]:
                return 1
            return 0
        
        low, high = 0, len(nums)-1

        while low < high:
            mid = (high+low)//2
            
            if nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                low = mid + 1
            
            else:
                high = mid
        
        if target <= nums[high]:
            return high
        
        return high+1
                

target = 2
nums = [1,3,5,6]
solution = Solution()
print(solution.searchInsert(nums, target))
