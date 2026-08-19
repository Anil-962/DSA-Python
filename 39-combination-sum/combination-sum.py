class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans =[]
        def fun(start,ren,temp):
            if ren ==0:
                ans.append(temp[::])
                return
            for i in range(start,len(candidates)):
                val=candidates[i]
                if val<=ren:
                    temp.append(val)
                    fun(i,ren-val,temp)
                    temp.pop()
        fun(0,target,[])
        return ans
