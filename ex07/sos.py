def get_morse_code_dict():
    """Returns a dictionary mapping alphanumeric characters and space to Morse
    code."""

    return {
        " ": "/",
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----."
    }


def validate_input(args):
    """Validates the input arguments.

    Args:
        args: List of command-line arguments.

    Raises:
        AssertionError: If the number of arguments is not 2 or if any character
        is invalid.
    """

    if len(args) != 2:
        raise AssertionError("the arguments are bad")

    morse_dict = get_morse_code_dict()
    for char in args[1].upper():
        if char not in morse_dict:
            raise AssertionError("the arguments are bad")


def convert_to_morse(input_string):
    """Converts the input string to Morse code.

    Args:
        input_string: The string to convert.

    Returns:
        A string representing the Morse code.
    """

    morse_dict = get_morse_code_dict()
    morse_code = ""
    for char in input_string.upper():
        morse_code += morse_dict[char] + " "
    return morse_code.strip()


def main():
    """Main function to execute the Morse code conversion."""

    import sys
    try:
        validate_input(sys.argv)
        input_string = sys.argv[1]
        morse_code = convert_to_morse(input_string)
        print(morse_code)
    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()
