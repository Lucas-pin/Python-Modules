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

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{path}'")

    try:
        print("---")
        file = open(path, "r", encoding="utf-8")
        content = file.read()
        if content:
            print(content, end="")
        print("\n---")

    except FileNotFoundError as ex:
        sys.stderr.write(f"Error: The file '{path}' does not exist.\n")
        sys.stderr.write(f"Details:{ex}\n")
    except PermissionError as ex:
        sys.stderr.write("[STDERR] Error: Insufficient permissions.\n")
        sys.stderr.write(f"[STDERR] Details:{ex}\n")
    except Exception as ex:
        sys.stderr.write(f"[STDERR] Error opening file '{path}'\n")
        sys.stderr.write(f"[STDERR] Details:{ex}\n")
    finally:
        if file is not None:
            file.close()
            print(f"File {path} closed.\n")

    try:
        if content:
            lines_2087 = [f"{line}#" for line in content.splitlines()]
            new_content = "\n".join(lines_2087)

            print("\nTransform data:")
            print("---")
            print(new_content)
            print("\n---")

            sys.stdout.write("Enter new file name (or empty):")
            sys.stdout.flush()
            name_new_file = sys.stdin.readline().rstrip()
            if name_new_file is not None and name_new_file != "":
                print(f"Saving data to '{name_new_file}'")
                new_file = open(name_new_file, "w", encoding="utf-8")
                new_file.write(new_content + "\n")
                new_file.close()
            else:
                print("Not saving data.")

    except Exception as ex:
        sys.stderr.write(f"[STDERR] Error saving data: {ex}\n")
        sys.stderr.write("[STDERR] Data not saved\n")
    finally:
        if new_file is not None:
            new_file.close()
