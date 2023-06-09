class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # given nums = [-2,1,-3,4,-1,2,1,-5,4]
        # output = 6
        # reason [4,-1,2,1] has the largest sum 6
        # seems pretty simple why is this a medium?
        # hint : Kadane's algo
        max_sum = nums[0] # smallest possible
        curr_sum = 0
        for i in nums:
            # reset if curr_sum of subarrays is ever negative
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += i 
            if curr_sum > max_sum:
                max_sum = curr_sum
            # max_sum = max(max_sum,curr_sum)
        return max_sum

