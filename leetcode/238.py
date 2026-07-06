class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        
        left = [1] * nums_len
        right = [1] * nums_len


        for i in range(1, nums_len):
            left[i] = left[i-1] * nums[i-1]

        for i in range(nums_len - 2, -1, -1):
            right[i] = right[i+1] * nums[i+1]

        answer = []
        for i in range(nums_len):
            answer.append(left[i] * right[i])

        return answer