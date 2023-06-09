class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        # nums = array of positive numbers, target is our goal
        # output = minimal legnth of subarray whose sum is greater or equal
        left,total = 0,0
        res = float("inf") # shortest total we find
        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                res = min(right - left + 1, res)
                # shifting
                total -= nums[left]
                left += 1
        return 0 if res == float("inf") else res