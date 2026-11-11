import typing
import sys


def transform_data(content: str) -> str:
    lines: list[str] = content.splitlines()
    transformed_lines: list[str] = [line + "#" for line in lines]
    if transformed_lines:
        return "\n".join(transformed_lines) + "\n"
    return ""


def recover_ancient_text(filename: str) -> None:
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    file: typing.IO[str] | None = None
    content: str = ""

    try:
        file = open(filename, "r")
        content = file.read()
    except OSError as err:
        print(f"Error opening file '{filename}': {err}")
        return
    finally:
        if file is not None:
            file.close()
            print(f"File '{filename}' closed.")

    print(content, end="" if content.endswith("\n") else "\n")

    transformed: str = transform_data(content)
    print("Transform data:")
    print(transformed, end="" if transformed.endswith("\n") else "\n")

    new_filename: str = input("Enter new file name (or empty): ").strip()
    if not new_filename:
        print("Not saving data.")
        return

    print(f"Saving data to '{new_filename}'")
    out_file: typing.IO[str] | None = None
    try:
        out_file = open(new_filename, "w")
        out_file.write(transformed)
        print(f"Data saved in file '{new_filename}'.")
    except OSError as err:
        print(f"Error saving file '{new_filename}': {err}")
    finally:
        if out_file is not None:
            out_file.close()


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return

    recover_ancient_text(sys.argv[1])


if __name__ == "__main__":
    main()
