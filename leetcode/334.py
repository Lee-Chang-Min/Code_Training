class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        result = False

        first = float('inf')
        second = float('inf')
        
        for n in nums:
            if n <= first:
                first = n
                continue

            elif n <= second:
                 second = n
                 continue

            else:
                result = True
                break
                
        return result

            