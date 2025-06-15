from ft_package import count_in_list


def main():
    print(count_in_list(["toto", "tata", "toto"], "toto"))  # ➜ 2
    print(count_in_list(["toto", "tata", "toto"], "tutu"))  # ➜ 0


if __name__ == "__main__":
    main()
