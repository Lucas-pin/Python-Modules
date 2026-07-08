def secure_archive(file_name: str,
                   operation: str | None = None,
                   content: str | None = None) -> tuple[bool, str]:
    if operation != "r" and operation != "w":
        return False, "Invalid operation"
    if (operation == "w" and content is None):
        return False, "The content must not be empty"

    try:
        with open(file_name, operation) as file:
            if (operation == "r"):
                return True, file.read()
            else:
                file.write(content)
                return True, str(content)
    except Exception as ex:
        return False, str(ex)


def main() -> None:
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", "r"))
    print()

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("inaccesible.txt", "r"))
    print()

    print("Using 'secure_archive' to read from a regular file:")
    print(secure_archive("ancient_fragment.txt", "r"))
    print()

    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("prueba.txt", "w", "Hola perrito malvado"))
    print()


if __name__ == "__main__":
    main()
