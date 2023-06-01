class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # my solution attempt to convert to a string since i see test case 2 x = -123 is false for 321-
        """return str(x) == str(x)[::-1]"""
        # followup can you do it without converting x into a string?
        # in the case of integers i think of placement manipulation
        # i.e. x//10 -> turns 123 into 12 and x%10 -> turns 123 into 23
        # edge case we know negative numbers cant be palindromes based on test case 2
        # and its kinda tricky to see but test case 3 is also a edge case
        if x < 0 or x != 0 and x%10 == 0:
            return False
        # after edge cases are done we move onto some integer checks
        # check is our reverse integer
        check = 0
        while x > check:
            check = check*10 + x%10
            x/=10
        # only need to check half
        # and x == check is for if x is even and the other one is when x is odd
        return x == check or x == check/10