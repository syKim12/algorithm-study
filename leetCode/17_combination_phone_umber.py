class Solution:
    def __init__(self):
        self.result = []
        return 

    def dfs(self, idx, digits, numbers, s):
        if len(s) == len(digits):
            self.result.append(s)
            return

        for char in numbers[digits[idx]]:
            self.dfs(idx+1, digits, numbers, s+char)

    def letterCombinations(self, digits: str) -> List[str]:
        numbers = {'2':['a', 'b', 'c'], '3':['d', 'e', 'f'], '4':['g', 'h', 'i'], '5':['j', 'k', 'l'], '6':['m', 'n', 'o'], '7':['p', 'q', 'r', 's'], '8':['t', 'u', 'v'], '9':['w', 'x', 'y', 'z']}


        self.dfs(0, digits, numbers, '')
        if len(self.result) == 1 and self.result[0] == '':
            return []
        return self.result