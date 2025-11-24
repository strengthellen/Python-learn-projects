def greeting(name="Ellen") -> str:
    return f"Hello, {name}!"


def main():
    name = input("What's your name? ").strip()
    if not name:
        name = "Ellen"

    print(greeting(name))


if __name__ == "__main__":
    main()