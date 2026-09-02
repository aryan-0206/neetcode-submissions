class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        window_sum = 0

        min_len = float('inf')

        for right in range(len(nums)):

            #Add Current Element
            window_sum += nums[right]

            #Shrink Window while sum is >= target
            while window_sum >= target:
                length = right - left + 1
                min_len = min(min_len, length)
                window_sum -= nums[left]
                left += 1
            
        if min_len == float('inf'):
            return 0

        return min_len