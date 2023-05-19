class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        # I/O -> s a string formed by digits 
        # want to map s to english lowercase characters
        # a - i -> 1 to 9
        # j - z -> 10# to 26#

        # so we are looking for 2 things either a single character that represents a to i or
        # a 3 character that represents a character j to z
        

        '''res = []
        i = len(s) - 1
        # while we still have characters to decrypt
        while i >= 0:
            # if we meet a unique identifer
            if s[i] == "#":
                # then we append that character by converting s[i-2:i] -> 10 from 10# into an integer from string then adding 96 because chr(10 is not an alphabet )
                res.append(chr(int(s[i-2:i])+96))
                # then we move index forward by 3
                i -= 3
            else:
                res.append(chr(int(s[i])+96))
                i -= 1
        return ''.join(res[::-1])'''

        dic = {'1':'a','2':'b','3':'c','4':'d','5':'e','6':'f','7':'g','8':'h','9':'i','10':'j','11':'k','12':'l','13':'m','14':'n','15':'o','16':'p','17':'q','18':'r','19':'s','20':'t','21':'u','22':'v','23':'w','24':'x','25':'y','26':'z'}

        length = len(s)
        i = 0
        ans = ''
        while i < length:
            if i+2 < length and s[i+2] == '#':
                ans += dic[s[i:i+2]]
                i += 3
            else: 
                ans += dic[s[i]]
                i += 1
        return ans
        # Using a dictionary to initalize a - z mapped by 1 to 26
        # initialize 3 variables to keep track of length, index, and our answer
        # we loop through the string s and we check if the current "encryption" is 3 characters long AND 
        # if the # exists
        # if it does we know its 10 - 26 meaning i to z and we add that to our answer via our dictionary
        # the logic is dic[key] where key is string[i:i+2] this grabs the first 2 characters but not the #
        # after we add we move the index past the 3 characters 
        # if the current "encryption" is not 3 characters we just assume its 1 and map that 
        # finally we return our answer