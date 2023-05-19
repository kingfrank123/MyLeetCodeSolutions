class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        MC = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        # 0 index , MC[0] = a, MC[1] = b .... 
        result = set()
        for word in words:
            word = word.lower()
            transformation = ""
            for ch in word:
                transformation += MC[ord(ch) - 97]
            result.add(transformation)
        return len(result)

        # return len({''.join([morse_code_array[ord(chr) - 97] for chr in word]) for word in words})