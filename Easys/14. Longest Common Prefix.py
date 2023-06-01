class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix=[]
        num = len(strs)
        for x in zip(*strs):
            # check if they have common prefix
            if len(set(x)) == 1:
                prefix.append(x[0])
            else:
                break
        # return common prefix in string form
        return "".join(prefix) 
        # while doing this problem i was thinking how to find consecutive prefixes anywhere in the string and came up with this
        '''prefix = []
        for i, char in enumerate(strs[0]):
            # Check if all other strings have the same character at index i
            if all(string[i] == char for string in strs[1:]):
                prefix.append(char)
            else:
                break

        # Return consecutive prefix in string form
        return "".join(prefix)'''