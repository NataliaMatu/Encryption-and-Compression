import math
from collections import Counter


def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        position = ord(char)
        if position < 255:
            encrypted_char = chr((position + shift) % 255)
        else:
            encrypted_char = char
        encrypted_text += encrypted_char
    return encrypted_text


def number_to_binary(x, length):
    binary = str(bin(x)[2:])
    binary = binary.rjust(length, "0")
    return binary


with open("generated.txt", "r") as file:
    text = file.read()

binary_text = ""
text_length = len(text)
print('Text length:', text_length)


def sorted_frequencies(text):
    char_count = Counter(text)
    sorted_chars = sorted(char_count, key=lambda x: char_count[x], reverse=True)
    return sorted_chars


sorted_chars = sorted_frequencies(text)
print(sorted_chars)
num_chars = len(sorted_chars)
N = math.ceil(math.log2(num_chars))

with open("compressed.txt", "w", encoding="utf-8") as compressed_file:
    compressed_file.write(chr(num_chars))

    for char in sorted_chars:
        compressed_file.write(char)
        print(char)

    padding = (8 - (3 + text_length * N) % 8) % 8
    binary_text = binary_text + number_to_binary(padding, 3)

    for char in text:
        binary_text = binary_text + number_to_binary(sorted_chars.index(char), N)

    binary_text = binary_text + ("1" * padding)
    print('Dictionary length(X):', len(sorted_chars))
    print('Padding(R):', padding)
    print('Character length(N):', N)

    encrypted_text = ""

    for i in range(0, len(binary_text), 8):
        segment = binary_text[i:i + 8]
        print(segment)
        encrypted_text += chr(int(segment, 2))

    shift = int(input('Enter shift for encryption: '))
    cipher_text = caesar_cipher(encrypted_text, shift)
    print('Encrypted:', cipher_text)
    compressed_file.write(cipher_text)

with open('cipher.txt', 'w') as cipher_file:
    cipher_file.write(str(shift))