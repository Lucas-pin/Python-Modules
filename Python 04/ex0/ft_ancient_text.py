import sys

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <file>")
else:
    path = sys.argv[1]
    file = None

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
