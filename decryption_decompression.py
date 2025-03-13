import math
import string

with open("cipher.txt", "r") as cipher_file:
    shift = int(cipher_file.read())


def decrypt_caesar(text, shift):
    decoded_text = ""
    for ch in text:
        position = ord(ch)
        shifted_position = position - shift
        if shifted_position < 0:
            shifted_position = 255 + (shifted_position % 255)
        decoded_text += chr(shifted_position)
    return decoded_text


with open('compressed.txt', 'r') as file:
    text = file.read()
    print(text)


def number_to_binary(x, display_length):
    binary = str(bin(x)[2:])
    binary = binary.rjust(display_length, "0")
    return binary


# The first character in the compressed file is the number of unique characters,
# followed by the encoding dictionary depending on the number of unique characters
num_characters = ord(text[0])
print('Number of unique characters: ', num_characters)
encoding_dictionary = text[1:num_characters + 1]
print('Character dictionary: ', encoding_dictionary)
encoded_chars = text[1 + num_characters:]
N = math.ceil(math.log2(num_characters))

encoding_map = {}

for char in encoding_dictionary:
    binary_representation = number_to_binary(encoding_dictionary.index(char), N)
    encoding_map[char] = binary_representation
print('Encoding dictionary: ', encoding_map)

binary_sequence = ''

decrypted_text = decrypt_caesar(encoded_chars, shift)

with open("decrypted.txt", 'w') as decrypted_file:
    decrypted_file.write(decrypted_text)

with open('decompressed.txt', 'w') as decompressed_file:
    index = 0
    while index < len(decrypted_text):
        ascii_char = ord(decrypted_text[index])
        print(ascii_char)
        binary_value = bin(ascii_char)[2:].zfill(8)
        print(binary_value)
        index += 1
        binary_sequence += binary_value

    remainder = int(binary_sequence[0:3], 2)
    encoded_sequence = binary_sequence[3:len(binary_sequence) - remainder]
    print('Remainder: ', remainder)

    decoded_output = ''
    i = 0
    while i < len(encoded_sequence):
        fragment = encoded_sequence[i:i + N]

        for letter, code in encoding_map.items():
            if code == fragment:
                decoded_output += letter
                break
        i += N

    decompressed_file.write(decoded_output)
    print("Decoded text:", decoded_output)
