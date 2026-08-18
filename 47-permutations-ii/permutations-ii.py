class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.ans=[]
        def fun(s):
            if s==len(nums):
                if nums not in self.ans:
                    self.ans.append(nums[::])
                return
            for i in range(s,len(nums)):
                nums[i],nums[s]=nums[s],nums[i]
                fun(s+1)
                nums[i],nums[s]=nums[s],nums[i]
        fun(0)
        return self.ans        