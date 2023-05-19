class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # keep track of all positive numbers and negative numbers
        # return max of the 2 
        # note: 0 is not positive or negative
        # bruteforce solution, not time efficent but very memory efficient
        """pos,neg = 0,0
        for v in nums:
            if v > 0:
                pos += 1
            elif v < 0:
                neg += 1
        return max(pos,neg)"""

        # time efficent but not memory efficient
        return max(len([x for x in nums if x > 0]),len([x for x in nums if x < 0]))