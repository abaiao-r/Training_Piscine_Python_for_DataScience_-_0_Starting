import sys


def is_upper(char):
    """Return True if char is an uppercase ASCII letter."""
    return 'A' <= char <= 'Z'


def is_lower(char):
    """Return True if char is a lowercase ASCII letter."""
    return 'a' <= char <= 'z'


def is_digit(char):
    """Return True if char is an ASCII digit."""
    return '0' <= char <= '9'


def is_space(char):
    """Return True if char is a space, tab, newline, or carriage return."""
    return char == ' ' or char == '\t' or char == '\n' or char == '\r'


def is_punct(char):
    """Return True if char is an ASCII punctuation character."""
    punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
    return char in punctuation


def count_char_types(text):
    """
    Count upper, lower, punctuation, spaces, and digits in the given text.
    Returns a dict with counts.
    """
    counts = {
        "upper": 0,
        "lower": 0,
        "punct": 0,
        "spaces": 0,
        "digits": 0
    }
    for char in text:
        if is_upper(char):
            counts["upper"] += 1
        elif is_lower(char):
            counts["lower"] += 1
        elif is_punct(char):
            counts["punct"] += 1
        elif is_space(char):
            counts["spaces"] += 1
        elif is_digit(char):
            counts["digits"] += 1
    return counts


def main():
    """
    Main function: parses arguments, prompts if needed, counts character types,
    and prints the results.
    """
    try:
        argc = len(sys.argv)
        if argc == 1 or (argc == 2 and (sys.argv[1] in (None, "", "None"))):
            text = input("What is the text to count?\n")
        elif argc == 2:
            text = sys.argv[1]
        else:
            raise AssertionError("Too many arguments")
        counts = count_char_types(text)
        print(f"The text contains {len(text)} characters:")
        print(f"{counts['upper']} upper letters")
        print(f"{counts['lower']} lower letters")
        print(f"{counts['punct']} punctuation marks")
        print(f"{counts['spaces']} spaces")
        print(f"{counts['digits']} digits")
    except AssertionError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
