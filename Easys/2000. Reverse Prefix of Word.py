class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        # given word = "abcdefd", ch = "d"
        # O/P -> "dcbaefd"(inclusive)
        # start at 0 and ends at first occurence of ch
        """start,end = 0,-1
        for i,v in enumerate(word):
            if v == ch:
                end = i
                break
        # found the end or ch don't exist in word
        if end == -1:
            return word
        # reverse operation
        return word[start:end+1][::-1] + word[end+1:len(word)]"""
        if ch not in word:
            return word
        else:
            i=word.find(ch)
            return (word[0:i+1])[::-1]+word[i+1:]
