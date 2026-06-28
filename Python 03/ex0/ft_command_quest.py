import sys

lenght: int = len(sys.argv)
i: int = 1
print("=== Command Quest ===")
print(f"Program name: {sys.argv[0]}")
if (lenght <= 1):
    print("No arguments provided!")
else:
    print(f"Arguments received: {lenght - 1}")
    while i < lenght:
        print(f"Argument {i}: {sys.argv[i]}")
        i += 1
print(f"Total arguments: {lenght}")
