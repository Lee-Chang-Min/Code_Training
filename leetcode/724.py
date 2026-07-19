class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        total = sum(nums)     # 전체 합, 한 번만 O(n)
        left_sum = 0          # 지금까지의 왼쪽 합
        
        for i in range (len(nums)):
            right_sum = total - nums[i] - left_sum

            if left_sum == right_sum:
                return i

            left_sum += nums[i]

        return -1

