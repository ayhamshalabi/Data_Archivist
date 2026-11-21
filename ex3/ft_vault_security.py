def secure_archive(
    file_name: str,
    action: str = "read",
    new_content: str = "",
) -> tuple[bool, str]:
    res: tuple[bool, str] = (False, f"Invalid action: '{action}'")
    try:
        if action == "read":
            with open(file_name, "r") as file:
                contant: str = file.read()
                res = (True, contant)
        elif action == "write":
            with open(file_name, "w") as file:
                file.write(new_content)
                res = (True, "Content successfully written to file")

    except OSError as err:
        return (False, f"{err}")

    return res


def main() -> None:
    print("=== Cyber Archives Security ===")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))

    print("")

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("inaccessible"))

    print("")

    print("Using 'secure_archive' to read from a regular file:")
    res: tuple[bool, str] = secure_archive("regular.txt")
    print(res)

    print("")

    if res[0]:
        print("Using 'secure_archive' to write previous content to a new file:")
        print(secure_archive("new_file.txt", "write", res[1]))


if __name__ == "__main__":
    main()
