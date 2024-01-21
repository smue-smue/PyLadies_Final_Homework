# Task:

# Objective: 

import argparse

parser = argparse.ArgumentParser(description="argparse greeting")
parser.add_argument("--input", help="input file", required=True)
parser.add_argument("--output", help="output file", required=True)
parser.add_argument("--offset", help="offset value", required=True)
parser.add_argument("--replacing_character", help="old character to be replaced", required=True)
parser.add_argument("--replacement_number", help="number to replace old character", required=True)
parser.add_argument("--indent", action="store_true", help="name will be indented by 4 spaces")

def cipher_ceasar(input, offset, indent=False):
    """Program that opens a file and saves the changes to another file."""
    i_handle = open(input, encoding="utf-8")

    int_offset = int(offset)

    new_line = ""
    ciphered_ceasar = ""

    with i_handle as input_file:
        for line in input_file:
            for char in line:
                if char.isupper():
                    char = chr((ord(char) - ord("A") + int_offset) % 26 + ord("A"))
                elif char.islower():
                    char = chr((ord(char) - ord("a") + int_offset) % 26 + ord("a"))
                new_line += char
        ciphered_ceasar += new_line
    
    return ciphered_ceasar

def cipher_number(result_ciphered_ceasar, replacing_character, replacement_number):

    transformed = ""

    try:
        replacement_number = int(replacement_number)
    except ValueError:
        print("You did not enter a number. Your invalid value is replaced with '1'.")
        replacement_number = 1

    replacements = {
        replacing_character.lower(): str(replacement_number),
        replacing_character.upper(): str(replacement_number)
    }
    
    for char in result_ciphered_ceasar:
        transformed += replacements.get(char, char)
    return transformed


# o_handle = open(output, mode="w", encoding="utf-8")
    # with o_handle as output_file:
    #     for line in ciphered:
    #         output_file.write(f"{line}\n")

args = parser.parse_args()

result_cipher_ceasar = cipher_ceasar(args.input, args.offset) # result is a string

result_cipher_number = cipher_number(result_cipher_ceasar, args.replacing_character, args.replacement_number)

print("\nCiphered Ceasar: \n")
print(result_cipher_ceasar)

print("\nCiphered Number: \n")
print(result_cipher_number)