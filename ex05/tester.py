import subprocess


def run_test(args, input_text=None):
    """
    Run building.py with given args and optional input_text.
    Print command, input, output, and errors.
    """
    cmd = ["python3", "building.py"] + args
    try:
        if input_text is not None:
            result = subprocess.run(
                cmd, input=input_text.encode(), capture_output=True, timeout=5
            )
        else:
            result = subprocess.run(
                cmd, capture_output=True, timeout=5
            )
        print("Command:", " ".join(cmd))
        if input_text is not None:
            print("Input:", repr(input_text))
        print("Output:\n", result.stdout.decode())
        if result.stderr:
            print("Errors:\n", result.stderr.decode())
        print("-" * 40)
    except Exception as e:
        print(f"Test failed: {e}")


def main():
    # 1. No argument, prompt user (simulate input)
    run_test([], input_text="Hello World!\n")
    # 2. One argument, normal string
    run_test(["Hello World!"])
    # 3. One argument, empty string (should prompt)
    run_test([""])
    # 4. One argument, "None" string (should prompt)
    run_test(["None"], input_text="Prompted input!\n")
    # 5. Two arguments, both non-empty (should concatenate and run)
    run_test(["Hello", "World!"])
    # 6. Two arguments, second is empty (should prompt)
    run_test(["Hello", ""], input_text="Prompted again!\n")
    # 7. Too many arguments (should error)
    run_test(["one", "two", "three"])
    # 8. Argument with explicit newline
    run_test(["Hello\nWorld!"])
    # 9. Long text
    run_test([
        "Python 3.0, released in 2008, was a major revision that is not "
        "completely backward-compatible with earlier versions. Python 2 "
        "was discontinued with version 2.7.18 in 2020."
    ])


if __name__ == "__main__":
    main()
