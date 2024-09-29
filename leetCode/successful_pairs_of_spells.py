
class Solution:
    def successfulPairs(self, spells, potions, success: int):    
        result = []
        potions.sort()
        for spell in spells:
            threshold = success/spell
            start = 0
            end = len(potions)
            while start <= end:
                mid = (start+end)//2
                if spell == 3:
                    print(start, end, mid)
                if mid == len(potions):
                    break
                if potions[mid] < threshold:
                        start = mid + 1
                elif potions[mid] == threshold :
                        break
                else:
                        end = mid - 1
            result.append(len(potions)-start)
          
        return result

s = Solution()
v = s.successfulPairs([5,1,3], [1,2,3,4,5], 7)        
print(v)