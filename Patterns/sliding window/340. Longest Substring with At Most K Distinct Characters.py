class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # iterating thru string s
        d = {}
        low, res = 0,0
        for i,ch in enumerate(s):
            d[ch] = i
            if len(d) > k:
                # need to shrink
                low = min(d.values())
                # low = lowest distinct value we shrink that
                del d[s[low]]
                low += 1
            res = max(i - low + 1, res)
        return res
        # this feels way harder than the average medium tbh