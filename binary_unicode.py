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

# Take input from user
message = input("Enter the message: ")

# Encode the message using Chuck Norris' method
encoded_message = chuck_norris_encode(message)

# Display the encoded message
print("Encoded message:", encoded_message)

def encode_message(message):
    encoded_message = ''
    for char in message:
        binary_char = format(ord(char), '07b')  # Convert character to 7-bit ASCII binary
        encoded_block = ''
        for bit in binary_char:
            if not encoded_block or encoded_block[-1] != bit:
                if encoded_block:
                    encoded_message += ' '  # Separate blocks with space
                encoded_message += '0' if bit == '1' else '00'  # Determine first block
            encoded_message += '0'  # Second block
        encoded_message += ' '  # Separate characters with space
    return encoded_message.strip()

# Take user input
message = input()

# Initialize an empty string to store the encoded message
encoded_message = ""

# Iterate through each character in the input message
for char in message:
    # Convert the ASCII value of the character to binary
    binary_char = bin(ord(char))[2:].zfill(7)
    
    # Initialize variables to store the current block and its count
    current_block = ""
    block_count = 0
    
    # Iterate through each bit in the binary representation of the character
    for bit in binary_char:
        # If the bit is the same as the current block, add it to the current block
        if bit == current_block:
            block_count += 1
        # If the bit is different from the current block, add the current block and its count to the encoded message
        else:
            # If the current block is '1', add '0' to the encoded message
            if current_block == '1':
                encoded_message += '0 '
            # If the current block is '0', add '00' to the encoded message
            else:
                encoded_message += '0 '
            # Add the number of '0's equal to the block count to the encoded message
            encoded_message += '0' * block_count + ' '
            
            # Update the current block and reset the block count
            current_block = bit
            block_count = 1
    
    # Add the last block and its count to the encoded message
    if current_block == '1':
        encoded_message += '0 '
    else:
        encoded_message += '0 '
    encoded_message += '0' * block_count + ' '

# Print the encoded message
print(encoded_message.strip())

outout 0  00 0 0 0000 0 00
expected 0 0 00 0000 0 00
