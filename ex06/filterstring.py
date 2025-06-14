import sys
from ft_filter import ft_filter


def main():
    """
    Main function to filter words longer than N from a string S.
    """
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")
        s = sys.argv[1]
        try:
            n = int(sys.argv[2])
        except Exception:
            raise AssertionError("the arguments are bad")
        words = s.split()
        result = list(ft_filter(lambda word: len(word) > n, words))
        print(result)
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
