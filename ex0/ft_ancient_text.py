import sys
import typing


def recover_ancient_text(filename: str) -> None:
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    file: typing.IO[str] | None = None
    try:
        file = open(filename, "r")
        content: str = file.read()
        print("---\n")
        print(content, end="" if content.endswith("\n") else "\n")
        print("\n---")
    except OSError as err:
        print(f"Error opening file '{filename}': {err}")
    finally:
        if file is not None:
            file.close()
            print(f"File '{filename}' closed.")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    recover_ancient_text(sys.argv[1])


if __name__ == "__main__":
    main()
