class Solution:
    def __init__(self):
        self.result = []
        return

    def dfs(self, prev,k, n, l):

        if len(l) == k:
            if sum(l) == n:
                self.result.append(l)
            return
        
        elif len(l) < k:
            for num in range(prev+1, 10):
                temp = l[:]
                temp.append(num)
                self.dfs(num, k, n, temp)
        return

    def bfs(self, k, n):

        return

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.dfs(0,k,n,[])
        return self.result
        