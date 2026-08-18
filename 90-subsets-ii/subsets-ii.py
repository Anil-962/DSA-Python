class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.ans=[]
        def fun(i,temp):
            if i==len(nums):
                if temp not in self.ans:
                    self.ans.append(temp[::])
                return
            fun(i+1,temp)
            fun(i+1,temp+[nums[i]])
        fun(0,[])
        return self.ans
        