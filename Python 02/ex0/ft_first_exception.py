def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    test_values = ["25", "abc"]
    for value in test_values:
        print(f"Input data is: {value}")
        try:
            result = input_temperature(value)
            if result is not None:
                print(f"Result: {result}\n")
        except (ValueError, OverflowError) as ex:
            print(f"Caught input_temperature error: {ex}\n")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
