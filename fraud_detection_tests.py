import fraud_detection as fd
import math


def test_ones_and_tens_digit_histogram():
    actual = fd.ones_and_tens_digit_histogram([127, 426, 28, 9, 90])
    expected = [0.2, 0.0, 0.3, 0.0, 0.0, 0.0, 0.1, 0.1, 0.1, 0.2]
    for i in range(len(actual)):
        assert math.isclose(actual[i], expected[i])
    assert sum(expected) == 1.0

    actual = fd.ones_and_tens_digit_histogram([0, 0, 0])
    expected = [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    for i in range(len(actual)):
        assert math.isclose(actual[i], expected[i])
    assert sum(expected) == 1.0

    actual = fd.ones_and_tens_digit_histogram([11, 11])
    expected = [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    for i in range(len(actual)):
        assert math.isclose(actual[i], expected[i])
    assert sum(expected) == 1.0

    actual = fd.ones_and_tens_digit_histogram([])
    expected = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    for i in range(len(actual)):
        assert math.isclose(actual[i], expected[i])


def main():
    test_ones_and_tens_digit_histogram()
    # call other test functions here


if __name__ == "__main__":
    main()
