from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm


def compare_docs():
    print("\033[96mComparing docstrings:\033[0m")
    builtin_doc = tqdm.__doc__
    custom_doc = ft_tqdm.__doc__
    color_green = "\033[92m"
    color_red = "\033[91m"
    color_reset = "\033[0m"
    match = builtin_doc == custom_doc
    print("tqdm docstring:\n", builtin_doc)
    print("ft_tqdm docstring:\n", custom_doc)
    print(
        f"Docstring match: {color_green if match else color_red}"
        f"{match}{color_reset}"
    )
    print("-" * 40)
    return match


def test_ft_tqdm():
    print("Testing ft_tqdm (custom):")
    for elem in ft_tqdm(range(50)):
        sleep(0.001)
    print("\033[92mft_tqdm ran (visual check required)\033[0m")


def test_tqdm():
    print("Testing tqdm (original):")
    for elem in tqdm(range(50)):
        sleep(0.001)
    print("\033[92mtqdm ran (visual check required)\033[0m")


def test_progress_bar_333():
    print("Test: Progress bar with 333 elements (ft_tqdm):")
    for elem in ft_tqdm(range(333)):
        sleep(0.005)
    print()
    print("Test: Progress bar with 333 elements (tqdm):")
    for elem in tqdm(range(333)):
        sleep(0.005)
    print()


def main():
    print("=== Docstring Test ===")
    doc_match = compare_docs()
    if doc_match:
        print("\033[92mDocstring test PASSED\033[0m")
    else:
        print("\033[91mDocstring test FAILED\033[0m")
    print("=== Progress Bar Test ===")
    print("Check visually if the two progress bars look similar.")
    test_ft_tqdm()
    test_tqdm()
    test_progress_bar_333()
    print(
        "\033[93mIf the progress bars are similar, test PASSED. "
        "Otherwise, test FAILED.\033[0m"
    )


if __name__ == "__main__":
    main()
