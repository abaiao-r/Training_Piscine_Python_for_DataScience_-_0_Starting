import subprocess
from ft_filter import ft_filter

# --- ft_filter tests ---


def compare_filters(func, iterable, description):
    """
    Compare ft_filter and built-in filter for the given function and iterable.
    Print results and whether they match.
    """
    expected = list(filter(func, iterable))
    result = list(ft_filter(func, iterable))
    print(description)
    print("Expected:", expected)
    print("ft_filter:", result)
    print("Match:", expected == result)
    print("-" * 40)


def test_ft_filter():
    compare_filters(lambda x: x % 2 == 0, [1, 2, 3, 4, 5],
                    "ft_filter: lambda x: x % 2 == 0 on [1,2,3,4,5]")
    compare_filters(None, [0, 1, '', 'abc', [], [1], False, True],
                    "ft_filter: None on [0, 1, '', 'abc', [], [1], False, "
                    "True]")
    compare_filters(str.isalpha, ['abc', '123', 'a1b2', 'xyz'],
                    "ft_filter: str.isalpha on ['abc', '123', 'a1b2', 'xyz']")
    compare_filters(None, [],
                    "ft_filter: None on [] (empty list)")
    compare_filters(lambda x: x > 10, range(20),
                    "ft_filter: lambda x: x > 10 on range(20)")

# --- filterstring.py tests ---


def run_filterstring(args):
    """
    Run filterstring.py with given args and return output.
    """
    cmd = ["python3", "filterstring.py"] + args
    result = subprocess.run(cmd, capture_output=True)
    return result.stdout.decode().strip()


def assert_filterstring(args, expected, description):
    output = run_filterstring(args)
    print(f"Test: {description}")
    print("Command:", "python3 filterstring.py", *args)
    print("Output:", output)
    print("Expected:", expected)
    print("Match:", output == expected)
    print("-" * 40)


def test_filterstring():
    assert_filterstring(
        ["Hello the World", "4"],
        "['Hello', 'World']",
        "words longer than 4"
    )
    assert_filterstring(
        ["Hello the World", "99"],
        "[]",
        "no words longer than 99"
    )
    assert_filterstring(
        ["3", "Hello the World"],
        "AssertionError: the arguments are bad",
        "wrong argument types"
    )
    assert_filterstring(
        [],
        "AssertionError: the arguments are bad",
        "no arguments"
    )
    assert_filterstring(
        ["Hello", "the", "World", "4"],
        "AssertionError: the arguments are bad",
        "too many arguments"
    )


def test_filter_docstring():
    print("Test: Compare ft_filter docstring with built-in filter docstring")
    from ft_filter import ft_filter
    builtin_doc = filter.__doc__
    my_doc = ft_filter.__doc__
    print("Built-in filter docstring:\n", builtin_doc)
    print("ft_filter docstring:\n", my_doc)
    if builtin_doc == my_doc:
        print("Match: True")
    else:
        print("Match: False")
        print("Diff:")
        import difflib
        for line in difflib.unified_diff(
            builtin_doc.splitlines(), my_doc.splitlines(),
            fromfile='filter.__doc__', tofile='ft_filter.__doc__', lineterm=''
        ):
            print(line)
    print("-" * 40)


def main():
    print("=== ft_filter docstring test ===")
    test_filter_docstring()
    print("=== ft_filter tests ===")
    test_ft_filter()
    print("=== filterstring.py tests ===")
    test_filterstring()


if __name__ == "__main__":
    main()
