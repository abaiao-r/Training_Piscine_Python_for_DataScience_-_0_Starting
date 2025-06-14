import subprocess


def run_sos(args, expected_output):
    cmd = ["python3", "sos.py"] + args
    result = subprocess.run(cmd, capture_output=True)
    output = result.stdout.decode().strip()
    color_green = "\033[92m"
    color_red = "\033[91m"
    color_reset = "\033[0m"
    match = output == expected_output
    color = color_green if match else color_red
    print("Command:", " ".join(cmd))
    print("Output:", output + "$")
    print("Expected:", expected_output + "$")
    print(f"Match: {color}{match}{color_reset}")
    print("-" * 40)


def test_sos_valid():
    run_sos(["sos"], "... --- ...")
    run_sos(["SOS"], "... --- ...")
    run_sos(["Hello World"], ".... . .-.. .-.. --- / .-- --- .-. .-.. -..")
    run_sos(["123"], ".---- ..--- ...--")
    run_sos(["a  b"], ".- / / -...")


def test_sos_invalid():
    run_sos(["h$llo"], "the arguments are bad")
    run_sos([], "the arguments are bad")
    run_sos(["hello", "world"], "the arguments are bad")
    run_sos([""], "")


def main():
    print("=== sos.py valid cases ===")
    test_sos_valid()
    print("=== sos.py invalid cases ===")
    test_sos_invalid()


if __name__ == "__main__":
    main()
