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


def test_mean_squared_error():
    actual = fd.mean_squared_error([1, 4, 9], [6, 5, 4])
    expected = 17.0
    assert math.isclose(actual, expected)

    actual = fd.mean_squared_error([2, 3, 4], [6, 5, 4])
    expected = 6.66666666667
    assert math.isclose(actual, expected)

    actual = fd.mean_squared_error([1, 4, 9], [2, 3, 4])
    expected = 9
    assert math.isclose(actual, expected)


def test_get_p_value():
    actual = fd.get_p_value(39)
    expected = 0.0039
    assert math.isclose(actual, expected)

    actual = fd.get_p_value(0)
    expected = 0.0
    assert math.isclose(actual, expected)


def main():
    test_ones_and_tens_digit_histogram()
    test_mean_squared_error()
    test_get_p_value()


if __name__ == "__main__":
    main()
