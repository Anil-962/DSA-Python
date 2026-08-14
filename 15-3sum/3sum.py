class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()  # Sort to handle duplicates and use pointers
        result = []
        n = len(nums)
        
        for i in range(n):
            if nums[i] > 0:
                break
                
            # Skip the exact same number to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            left, right = i + 1, n - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicate values for 'left' and 'right' pointers
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                        
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1  # Sum is too low, move left pointer to increase it
                else:
                    right -= 1  # Sum is too high, move right pointer to decrease it
                    
        return result
