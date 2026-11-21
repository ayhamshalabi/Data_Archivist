import sys
from typing import IO


def read_file(file_name: str) -> str | None:
    file: IO[str] | None = None
    contant: str | None = None
    try:
        file = open(file_name)
        contant = file.read()

        print("---")
        print(contant, end="")
        print("---")

    except IOError as err:
        print(f"Error opening file '{sys.argv[1]}': {err}")

    finally:
        if file is not None:
            file.close()
            print(f"File '{file_name}' closed.")

    if contant is not None:
        return contant
    return None


def transform_data(contant: str) -> None:
    new_contant: list[str] = [line + "#\n" for line in contant.splitlines()]

    print("---")
    for line in new_contant:
        print(line, end="")
    print("---")

    new_file_name: str = input("Enter new file name (or empty): ")
    if new_file_name == "":
        print("Not saving data.")
        return
    else:
        print(f"Saving data to '{new_file_name}'")

    new_file: IO[str] | None = None
    try:
        new_file = open(new_file_name, "w")
        for line in new_contant:
            new_file.write(line)

        print(f"Data saved in file {new_file_name}.")

    except IOError:
        print(f"Error opening file '{new_file_name}'")

    finally:
        if new_file is not None:
            new_file.close()


def ft_archive_creation() -> None:
    if len(sys.argv) < 2:
        print("Usage: ft_archive_creation.py <file>")
        return

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{sys.argv[1]}'")

    contant: str | None = read_file(sys.argv[1])

    if contant is not None:
        transform_data(contant)


if __name__ == "__main__":
    ft_archive_creation()
