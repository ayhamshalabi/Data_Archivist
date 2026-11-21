def ft_vault_security(
    file_name: str,
    action: str = "read",
    new_content: str = "",
) -> tuple[bool, str]:
    try:
        with open(file_name, "r+") as file:
            contant: str = file.read()
            if action == "write":
                file.write(new_content)
                return (True, "Content successfully written to file")

    except IOError as err:
        return (False, f"{err}")

    return (True, contant)


def main() -> None:
    print("=== Cyber Archives Security ===")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(ft_vault_security("/not/existing/file"))

    print("")

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(ft_vault_security("inaccessible"))

    print("")

    print("Using 'secure_archive' to read from an regular file:")
    res = ft_vault_security("regular.txt")
    print(res)

    print("")

    print("Using 'secure_archive' to write previous content to a new file:")
    print(ft_vault_security("new_file.txt", "write", res[1]))


if __name__ == "__main__":
    main()
