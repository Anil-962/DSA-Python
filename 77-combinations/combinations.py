class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.ans=[]
        def fun(s,t):
            if len(t)==k:
                self.ans.append(t[::])
                return
            for i in range(s,n+1):
                t.append(i)
                fun(i+1,t)
                t.pop()

        fun(1,[])
        return self.ans

        