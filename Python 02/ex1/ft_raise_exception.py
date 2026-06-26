def input_temperature(temp_str: str) -> int:
    temp: int = int(temp_str)
    if (0 <= temp <= 40):
        return temp
    elif (temp < 0):
        raise ValueError(f"{temp} is too cold for plants (min 0°C)")
    else:
        raise ValueError(f"{temp} is too hot for plants (max 40°C)")


def test_temperature() -> None:
    test_values = ["25", "abc", "-5", "45"]
    for value in test_values:
        print(f"Input data is: {value}")
        try:
            result = input_temperature(value)
            if result is not None:
                print(f"Result: {result}\n")
        except (ValueError, OverflowError) as ex:
            print(f"Caught input_temperature error: {ex}\n")
    print("All tests completed - program didn't crash!")


def main() -> None:
    test_temperature()


if __name__ == "__main__":
    main()
