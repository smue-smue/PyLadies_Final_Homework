# Task:

# Objective: 

import argparse

parser = argparse.ArgumentParser(
    description="""
    This script performs a Caesar cipher encryption on the text in the input file. 
    It then replaces specified characters with a given number and saves the result to an output file.
    
    Example usage:
    python your_script_name.py --in_file input.txt --out_file output.txt --offset 5 --replacing_character X --replacement_number 3 --indent
    """,
    formatter_class=argparse.RawTextHelpFormatter) # formatting mulitline message
parser.add_argument("--in_file", help="input file", required=True)
parser.add_argument("--out_file", help="output file", required=True)
parser.add_argument("--offset", help="offset value", required=True, type=int)
parser.add_argument("--replacing_character", help="old character to be replaced", required=True)
parser.add_argument("--replacement_number", help="number to replace old character", required=True, type=int)
parser.add_argument("--indent", action="store_true", help="name will be indented by 4 spaces")

# 1st changes - ceasars cipher, moving characters by a given offset

def cipher_ceasar(in_file, offset):
    """Opens input file and performs a Ceasar's cipher,
    each letter is shifted by the offset number up the alphabet."""
 
    try:
        int_offset = int(offset)
    except ValueError:
        print("You did not enter a number. Your invalid value is replaced with '1'.")
        int_offset = 1

    int_offset = int(offset)

    try: 
        with open(in_file, encoding="utf-8") as input_file:
            ciphered_ceasar = ""
            for line in input_file:
                new_line = ""
                for char in line:
                    if char.isupper():
                        char = chr((ord(char) - ord("A") + int_offset) % 26 + ord("A"))
                    elif char.islower():
                        char = chr((ord(char) - ord("a") + int_offset) % 26 + ord("a"))
                    new_line += char
                ciphered_ceasar += new_line
        input_file.close()
        return ciphered_ceasar
    except OSError as e:
        print(f"Error opening input file: {e}")
        return None

# 2nd changes - replacing given characters with numbers

def cipher_number(result_ciphered_ceasar, replacing_character, replacement_number):
    """Takes the result of the Ceasar's cipher, replaces letters
    by a certain number - both specified by the user."""

    ciphered_number = ""

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
        ciphered_number += replacements.get(char, char)
    return ciphered_number

# Saving the final version to a new file

def save_to_new_file(result_cipher_number, out_file):
    """Takes the final cipher result and saves it to the output file,
    as specified by the user."""

    try:
        with open(out_file, mode="w", encoding="utf-8") as output_file:
            output_file.write(result_cipher_number)
        output_file.close()
    except OSError as e:
        print(print(f"Error opening output file: {e}"))

# MAIN SCRIPT

args = parser.parse_args()

result_cipher_ceasar = cipher_ceasar(args.in_file, args.offset) # result is a string

result_cipher_number = cipher_number(result_cipher_ceasar, args.replacing_character, args.replacement_number) # result is a string

save_to_new_file(result_cipher_number, args.out_file)

print("\nCiphered Ceasar: \n")
print(result_cipher_ceasar)

print("\nCiphered Number: \n")
print(result_cipher_number)