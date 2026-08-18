class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans=[]
        def fun(s):
            if s==len(nums):
                self.ans.append(nums[::])
                return
            for i in range(s,len(nums)):
                nums[i],nums[s]=nums[s],nums[i]
                fun(s+1)
                nums[i],nums[s]=nums[s],nums[i]
        fun(0)
        return self.ans        