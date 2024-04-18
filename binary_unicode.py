def encode_binary(message):
    binary_message = ''.join(format(ord(char), 'b') for char in message) # Convert each character to its binary representation
    encoded_message = binary_message.replace('1', '0') # Replace all '1's with '0's
    return encoded_message

# Test the function
message = input("Enter the message to encode: ")
encoded_message = encode_binary(message)
print("Encoded message:", encoded_message)