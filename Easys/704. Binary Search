class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        '''for i,v in enumerate(nums):
            if target == v:
                return i
        return -1'''
        # slow and fast pointer

        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2

            # we are allowed to just get rid of half of the searches at every search interval because it is a sorted array
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
    
        # most efficient solution because of divide and conquer technique O(logn)