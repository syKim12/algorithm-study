#https://security-nanglam.tistory.com/445
def permute(nums, r):
    results = []
    prev_elements = []
    def dfs(elements):
        if len(elements) == (len(nums) - r):
            print(elements, len(nums)-r)
            results.append(prev_elements[:])
        for e in elements:
            next_elements = elements[:]
            next_elements.remove(e)

            prev_elements.append(e)
            dfs(next_elements)
            prev_elements.pop()
    dfs(nums)
    return results

print(permute([1,2,3],2))




