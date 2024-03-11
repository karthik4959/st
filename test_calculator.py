from calculator import Calculator

calculator = Calculator()


def test(a, b, expected_result):
    result = calculator.add(a, b)
    if result == expected_result:
        print("Addition test passed")
    else:
        raise ValueError("Addition test failed. Expected:", expected_result, "but got:", result)


test(4, 2, 6)
""" correct expected out put the build will pass"""
