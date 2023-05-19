class Solution(object):
    def maximumValue(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        big = 0
        for i in strs:
            if i.isdigit():
                big = max(big,int(i))
            else:
                big = max(big,len(i))


        return big
        # isalpha
        # isdigit