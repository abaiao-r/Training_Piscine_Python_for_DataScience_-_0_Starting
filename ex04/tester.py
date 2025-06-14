import os

tests = [
    ["14"],
    ["-5"],
    [],
    ["0"],
    ["Hi!"],
    ["13", "5"]
]

for args in tests:
    cmd = ["python3", "whatis.py"] + args
    print(f"$> python whatis.py{' ' if args else ''}{' '.join(args)}")
    os.system(' '.join(cmd))
    print("$>")
