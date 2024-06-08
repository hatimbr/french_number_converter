from .converter import FrenchConverter


def cli():
    converter = FrenchConverter()
    number = ""

    while number != "exit":
        number = input("Enter a number: ")
        if number == "exit":
            break
        elif not number.isdigit():
            print("Invalid input")
            continue

        result = converter.convert(int(number))
        print(result)


def convert_list(numbers):
    converter = FrenchConverter()
    results = []

    for number in numbers:
        result = converter.convert(number)
        results.append(result)

    return results


if __name__ == "__main__":
    cli()