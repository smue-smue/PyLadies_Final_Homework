# Task: Cipher Tool

# Objective: Apply cipher techniques to a given .txt-file,
# saving it to another .txt-file. Use command-line interface that allows 
# users to specify input files, output files, cipher offset, 
# characters to be replaced, and their numerical replacements,
# and if they want to insert animal names at random positions.

import argparse
import random

parser = argparse.ArgumentParser(
    description="""
    This script performs a Caesar cipher encryption on the text in the input file. 
    It then replaces specified characters with a given number and saves the result to an output file.
    
    Example usage:
    python your_script_name.py --in_file input.txt --out_file output.txt --offset 5 
    --replacing_character X --replacement_number 3 --indent
    """,
    formatter_class=argparse.RawTextHelpFormatter) # formatting mulitline message
parser.add_argument("-i", "--in_file", 
                    help="Path to the input file. This file contains the text to be processed.", 
                    required=True)
parser.add_argument("-o", "--out_file", 
                    help="Path to the output file. The processed text will be saved to this file.", 
                    required=True)
parser.add_argument("--offset", 
                    help="Offset value for the Caesar cipher. It specifies how many positions each letter will be shifted in the alphabet.", 
                    required=True, 
                    type=int)
parser.add_argument("--replacing_character",
                    help="The character in the text that will be replaced.", 
                    required=True)
parser.add_argument("--replacement_number", 
                    help="The number that will replace each occurrence of the specified character.", 
                    required=True, 
                    type=int)
parser.add_argument("--animal",
                    action="store_true",
                    help="If set, an random animal name will be put into random position in the text.")
parser.add_argument("--indent", 
                    action="store_true", 
                    help="If set, the output will be indented by 4 spaces.")

# 1st changes

def cipher_ceasar(in_file, offset):
    """Opens input file and performs a Ceasar's cipher,
    each letter is shifted by the offset number up the alphabet."""
 
    try:
        int_offset = int(offset)
    except ValueError:
        print("You did not enter a number. Your invalid value is replaced with '1'.")
        int_offset = 1

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

# 2nd changes

def cipher_number(result_ciphered_ceasar, replacing_character, replacement_number):
    """Takes the result of the 1st cipher, replaces letters
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

# 3rd changes

def cipher_animal(result_cipher_number, animal):
    """ If set, takes the result of the 2nd Cipher, replaces word at a randomly chosen 
    position in each line with a randomly chosen animal. Destroys text."""

    animals = [
        "Antelope", "Bear", "Cheetah", "Dolphin", "Elephant", "Flamingo",
        "Giraffe", "Hippopotamus", "Iguana", "Jaguar", "Kangaroo", "Lion",
        "Monkey", "Narwhal", "Octopus", "Penguin", "Quokka", "Rabbit",
        "Shark", "Tiger", "Urchin", "Vulture", "Walrus", "Xerus", "Yak", "Zebra"
    ]
    
    if animal:
        lines = result_cipher_number.splitlines() # Split string text to List item - line per line
        animal_select = random.choice(animals)

        for i, line in enumerate(lines):
            lst_line = line.split()
            if lst_line: # Check if the line is not empty
                number_select = random.randint(0, len(lst_line) - 1) # Choses random position at each line
                lst_line[number_select] = animal_select
                lines[i] = " ".join(lst_line)
        
        mod_text = "\n".join(lines)
        return mod_text

    return result_cipher_number # if animal is not set, returns unchanged result of 2nd cipher

# Saving the final version to a new file

def save_to_new_file(result_cipher_animal, out_file, indent=False):
    """Takes the final cipher result and saves it to the output file,
    as specified by the user."""

    try:
        with open(out_file, mode="w", encoding="utf-8") as output_file:
            mod_text = ""
            if indent:
                lines = result_cipher_animal.splitlines() # Split string text to List item - line per line
                # print(lines) ## P ##
                for line in lines:
                    line = "    " + line
                    # print(line) ## P ##
                    mod_text += line + "\n"
                # print(mod_text) ## P ##
                output_file.write(mod_text)
            else:
                output_file.write(result_cipher_animal)
        output_file.close()

    except OSError as e:
        print(print(f"Error opening output file: {e}"))

def main():
    """Main function for the cipher tool script.

    The script accepts input and output file paths, offset for the Caesar cipher,
    characters to be replaced, replacement numbers, and a flag to insert random 
    animal names through command-line arguments.
    
    The script starts by parsing command-line arguments using argparse 
    and then applies the three cipher transformations iteratively to the 
    transformed text of the input file. The final ciphered text is saved to an output file."""

    # Parse CLI arguments
    args = parser.parse_args()

    # Apply ciphers
    result_cipher_ceasar = cipher_ceasar(args.in_file, args.offset) # result is a string
    result_cipher_number = cipher_number(result_cipher_ceasar, args.replacing_character, args.replacement_number) # result is a string
    result_cipher_animal = cipher_animal(result_cipher_number, args.animal)

    # Save to file
    save_to_new_file(result_cipher_animal, args.out_file, args.indent)

    # Print results for debugging

    #print("\nCiphered Ceasar: \n")
    #print(result_cipher_ceasar)

    #print("\nCiphered Number: \n")
    #print(result_cipher_number)

    #print("\nCiphered Animal: \n")
    #print(result_cipher_animal)

if __name__ == "__main__":
    main()