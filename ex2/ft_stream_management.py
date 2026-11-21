import sys
from typing import IO


def read_file(file_name: str) -> str | None:
    file: IO[str] | None = None
    content: str | None = None
    try:
        file = open(file_name)
        content = file.read()

        print("---")
        print(content, end="" if content.endswith("\n") else "\n")
        print("---")

    except OSError as err:
        print(
            f"[STDERR] Error opening file '{file_name}': "
            f"{err}",
            file=sys.stderr
        )

    finally:
        if file is not None:
            file.close()
            print(f"File '{file_name}' closed.")

    return content


def transform_data(content: str) -> None:
    print("Transform data:")
    new_content: list[str] = [line + "#\n" for line in content.splitlines()]

    print("---")
    for line in new_content:
        print(line, end="")
    print("---")

    print("Enter new file name (or empty): ", file=sys.stdout, end="")
    sys.stdout.flush()
    new_file_name: str = sys.stdin.readline().strip("\n")

    if new_file_name == "":
        print("Not saving data.")
        return
    print(f"Saving data to '{new_file_name}'")

    new_file: IO[str] | None = None
    try:
        new_file = open(new_file_name, "w")
        for line in new_content:
            new_file.write(line)

        print(f"Data saved in file '{new_file_name}'.")

    except OSError as err:
        print(
            f"[STDERR] Error opening file '{new_file_name}': "
            f"{err}",
            file=sys.stderr
        )
        print("Data not saved.")

    finally:
        if new_file is not None:
            new_file.close()


def ft_archive_creation() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
        return

    print("=== Cyber Archives Recovery & Preservation ===")

    filename: str = sys.argv[1]
    print(f"Accessing file '{filename}'")
    content: str | None = read_file(filename)

    if content is not None:
        transform_data(content)


if __name__ == "__main__":
    ft_archive_creation()
