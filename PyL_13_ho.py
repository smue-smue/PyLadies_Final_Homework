# Task:

# Objective: 

import argparse

parser = argparse.ArgumentParser(description="argparse greeting")
parser.add_argument("--input", help="input file", required=True)
parser.add_argument("--output", help="output file", required=True)
parser.add_argument("--offset", help="offset value", required=True)
parser.add_argument("--replace_old", help="old character to be replaced", required=True)
parser.add_argument("--replace_new", help="number to replace old character", required=True)
parser.add_argument("--indent", action="store_true", help="name will be indented by 4 spaces")

def cipher_ceasar(input, output, offset, indent=False):
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

def cipher_number(ciphered_ceasar, replace_new, replace_old):

    ciphered_number = ""

    try:
        replace_new = int(args.replace_new)
    except:
        print("You did not enter a number. Your invalid value is replaced with '1'.")
        replace_new = 1

    replace_old = args.replace_old.lower()

    for line in ciphered_ceasar:
        new_line = line.split()
        for word in new_line:
            word.replace(replace_old, replace_new)
            new_line += word

        ciphered_number += new_line



# o_handle = open(output, mode="w", encoding="utf-8")
    # with o_handle as output_file:
    #     for line in ciphered:
    #         output_file.write(f"{line}\n")

args = parser.parse_args()

ciphered_ceasar = cipher_ceasar(args.input, args.output, args.offset, args.indent)
ciphered_number = cipher_number(ciphered_ceasar, args.replace_new, args.replace_old)

print("\n Ciphered Ceasar: \n")
print(ciphered_ceasar)
print("\n Ciphered Number: \n")
print(ciphered_number)