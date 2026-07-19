class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        result = gain[0]
        curr = gain[0]

        for i in range(1, len(gain)):
            next1 = curr + gain[i]

            result = max(result, next1)

            curr = next1

        if result < 0:
            return 0
        return result


    
        