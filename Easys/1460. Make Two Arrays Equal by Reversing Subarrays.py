class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        # sort both arrays
        target.sort(reverse=True)
        arr.sort(reverse=True)
        if target==arr:
            return True
        else:
            return False