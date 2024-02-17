#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Add two integers.

    Parameters:
    - a: int or float, first number to add
    - b: int or float, second number to add (default is 98)

    Returns:
    - int, the sum of a and b

    Raises:
    - TypeError: If a or b is not an integer or float
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    a = int(a)
    b = int(b)

    return a + b


def run_tests():
    with open('tests/0-add_integer.txt', 'r') as f:
        for line in f:
            test_input, expected_output = line.strip().split(';')
            test_input = [
                float(x) if '.' in x else int(x) for x in test_input.split(',')
            ]
            result = add_integer(*test_input)
            try:
                expected_output = float(
                    expected_output) if '.' in expected_output else int(
                        expected_output)
                assert result == expected_output
                print(f"Test passed: {test_input} => {expected_output}")
            except AssertionError:
                print(
                    f"Test failed: {test_input} => {expected_output}, got {result}"
                )


if __name__ == '__main__':
    run_tests()
