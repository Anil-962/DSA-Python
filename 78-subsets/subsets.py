class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        def fun(i,temp):
            if i ==len(nums):
                self.ans.append(temp[::])
                return
            fun(i+1,temp)
            fun(i+1,temp+[nums[i]])
        fun(0,[])
        return self.ans        