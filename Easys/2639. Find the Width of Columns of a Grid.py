class Solution(object):
    def findColumnWidth(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        res = []
        # we want to run through columns
        for i in range(len(grid[0])):
            seen = 1
            for j in range(len(grid)):
                # len(str(grid[j][i])) is what we are comparing
                seen = max(seen,len(str(grid[j][i])))
            res.append(seen)
        return res
        # this took me like 10 mins