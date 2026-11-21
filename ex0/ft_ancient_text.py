import sys
from typing import IO


def ft_ancient_text() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    print("=== Cyber Archives Recovery ===")

    filename: str = sys.argv[1]
    print(f"Accessing file '{filename}'")

    file: IO[str] | None = None
    try:
        file = open(filename, "r")
        content: str = file.read()

        print("---")
        print(content, end="" if content.endswith("\n") else "\n")
        print("---")

    except OSError as err:
        print(f"Error opening file '{filename}': {err}")

    finally:
        if file is not None:
            file.close()
            print(f"File '{filename}' closed.")


if __name__ == "__main__":
    ft_ancient_text()
