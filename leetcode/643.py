class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:


        max_1 = sum(nums[:k])   # 첫 구간 합을 실제 값으로
        window = max_1

        for i in range(k, len(nums)):
            window += nums[i]
            window -= nums[i-k]          
            max_1 = max(max_1, window)



        return max_1 / k


        