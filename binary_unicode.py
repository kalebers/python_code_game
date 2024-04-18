"""
Binary with 0 and 1 is good, but binary with only 0, or almost, is even better! Originally, this is a concept designed by Chuck Norris to send so called unary messages.
Write a program that takes an incoming message as input and displays as output the message encoded using Chuck Norris’ method.
Encoding principle:
The input message consists of ASCII characters (7-bit)
The encoded output message consists of blocks of 0
A block is separated from another block by a space
Two consecutive blocks are used to produce a series of same value bits (only 1 or 0 values):
- First block: it is always 0 or 00. If it is 0, then the series contains 1, if not, it contains 0
- Second block: the number of 0 in this block is the number of bits in the series
Several tests show this code is proper:
 1) input: C
    output: 0 0 00 0000 0 00
 2) input: CC
    output: 0 0 00 0000 0 000 00 0000 0 00
 3) input: %
    output: 00 0 0 0 00 00 0 0 00 0 0 0
 4) input: Chuck Norris' keyboard has 2 keys: 0 and white space
    output: 0 0 00 0000 0 0000 00 0 0 0 00 000 0 000 00 0 0 0 00 0 0 000 00 000 0 0000 00 0 0 0 00 0 0 00 00 0 0 0 00 00000 0 0 00 00 0 000 00 0 0 00 00 0 0 0000000 00 00 0 0 00 0 0 000 00 00 0 0 00 0 0 00 00 0 0 0 00 00 0 0000 00 00 0 00 00 0 0 0 00 00 0 000 00 0 0 0 00 00000 0 00 00 0 0 0 00 0 0 0000 00 00 0 0 00 0 0 00000 00 00 0 000 00 000 0 0 00 0 0 00 00 0 0 000000 00 0000 0 0000 00 00 0 0 00 0 0 00 00 00 0 0 00 000 0 0 00 00000 0 00 00 0 0 0 00 000 0 00 00 0000 0 0000 00 00 0 00 00 0 0 0 00 000000 0 00 00 00 0 0 00 00 0 0 00 00000 0 00 00 0 0 0 00 0 0 0000 00 00 0 0 00 0 0 00000 00 00 0 0000 00 00 0 00 00 0 0 000 00 0 0 0 00 00 0 0 00 000000 0 00 00 00000 0 0 00 00000 0 00 00 0000 0 000 00 0 0 000 00 0 0 00 00 00 0 0 00 000 0 0 00 00000 0 000 00 0 0 00000 00 0 0 0 00 000 0 00 00 0 0 0 00 00 0 0000 00 0 0 0 00 00 0 00 00 00 0 0 00 0 0 0 00 0 0 0 00 00000 0 000 00 00 0 00000 00 0000 0 00 00 0000 0 000 00 000 0 0000 00 00 0 0 00 0 0 0 00 0 0 0 00 0 0 000 00 0
"""



def chuck_norris_encode(message):
    encoded_message = ""
    for char in message:
        # Convert the character to its ASCII representation
        ascii_value = ord(char)
        
        # Convert the ASCII value to binary representation
        binary_value = bin(ascii_value)[2:].zfill(7)
        
        # Apply Chuck Norris' encoding principle
        encoded_block = ""
        prev_bit = None
        for bit in binary_value:
            if bit != prev_bit:
                if encoded_block:
                    encoded_message += " "
                if bit == "0":
                    encoded_message += "00 0"
                else:
                    encoded_message += "0 0"
                encoded_block = "0"
            else:
                encoded_block += "0"
            prev_bit = bit
        
        encoded_message += " " + encoded_block
        
    return encoded_message

# Test cases
test_cases = ["C", "CC", "%", "Chuck Norris' keyboard has 2 keys: 0 and white space"]
for test_case in test_cases:
    print("input:", test_case)
    print("output:", chuck_norris_encode(test_case))
    print()