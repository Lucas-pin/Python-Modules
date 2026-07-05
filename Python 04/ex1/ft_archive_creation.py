import sys


if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <file>")
else:
    path = sys.argv[1]
    file = None
    content: str | None = None
    new_content: str | None = None
    name_new_file: str | None = None
    new_file = None

    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{path}'")

    try:
        print("---")
        file = open(path, "r", encoding="utf-8")
        content = file.read()
        if content:
            print(content, end="")
        print("\n---")

    except FileNotFoundError as ex:
        print(f"Error: The file '{path}' does not exist. Details:{ex}")
    except PermissionError as ex:
        print(f"Error: You do not have the required permissions. Details:{ex}")
    except Exception as ex:
        print(f"Error opening file '{path}': {ex}")
    finally:
        if file is not None:
            file.close()
            print(f"File {path} closed.")

    try:
        if content:
            lines_2087 = [f"{line}#" for line in content.splitlines()]
            new_content = "\n".join(lines_2087)

            print("\nTransform data:")
            print("---")
            print(new_content)
            print("\n---")

            name_new_file = input("Enter new file name (or empty):")
            if name_new_file is not None and name_new_file != "":
                new_file = open(name_new_file, "w", encoding="utf-8")
                new_file.write(new_content + "\n")
                new_file.close()
            else:
                print("Not saving data.")

    except Exception as ex:
        print(f"Error saving data: {ex}")
