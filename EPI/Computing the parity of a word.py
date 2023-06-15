# parity of a binary wor dis 1 if the number of 1s in the word is odd otherwise 0
# parity of 1101 is 1, and parity of 10001000 is 0
# parity checks used to detect single bit errors in data storage and communication (such as the hamming code)
# write the program that computes the pairty of a 64-bit word
def parity(x: int) -> int:
    # TODO - you fill in here. 4.1
    # input is a 64-bit word, res stores the parity of bits in x is even(0) or odd(1)
    res = 0
    # while x isn't 0
    while x:
        # ^ is the XOR bitwise operation
        res ^= 1
        # shift x to the right since we have our LSB
        # x >>= 1
        # lowest set bit trick
        # x = x&(x-1)
        x &= x - 1
    return res
# so 1 is odd and 0 otherwise(even)