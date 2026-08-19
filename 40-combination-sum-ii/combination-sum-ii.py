class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans =[]
        def fun(start,ren,temp):
            if ren ==0:
                ans.append(temp[::])
                return
            for i in range(start,len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                val=candidates[i]
                if val>ren:
                    break
                temp.append(val)
                fun(i+1,ren-val,temp)
                temp.pop()
        fun(0,target,[])
        return ans

        