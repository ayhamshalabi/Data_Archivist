import sys
from typing import IO


def ft_ancient_text() -> None:
    if len(sys.argv) < 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file {sys.argv[1]}")

    file: IO[str] | None = None
    try:
        file = open(sys.argv[1])
        content: str = file.read()

        print("---")
        print(content, end="")
        print("---")

    except OSError as err:
        print(f"Error opening file '{sys.argv[1]}': {err}")

    finally:
        if file is not None:
            file.close()
            print(f"File '{sys.argv[1]}' closed.")


if __name__ == "__main__":
    ft_ancient_text()
