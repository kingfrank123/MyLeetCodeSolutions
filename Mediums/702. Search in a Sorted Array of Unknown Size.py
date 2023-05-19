# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """

class Solution(object):
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        """outOfBounds = 2**31 - 1
        i = 0
        while reader.get(i) != outOfBounds:
            if reader.get(i) == target:
                return i
            i += 1
        return -1"""
        # this previous solution is beats most in memory but not in time efficently 
        # so while rereading this problem i realized i can use maxiumum length of the array as the length vs the out of bounds as the limit
        l, r = 0, 10000
        while l <= r:
            mid = (l+r)//2
            val = reader.get(mid)
            if val == target: 
                return mid
            elif val < target: 
                l = mid+1
            else: 
                r = mid-1 
        return -1
        # using binary search as a template