def test_addition():
    assert 2 + 2 == 4


def test_addition_negative():
    assert not 2 + 2 == 5


def test_string_concatenation():
    assert "hello" + " " + "world" == "hello world"


def test_multiplication():
    assert 3 * 4 == 12


def test_list_sort():
    my_list = [3, 1, 4, 1, 5, 9, 2, 6]
    my_list.sort()
    assert my_list == [1, 1, 2, 3, 4, 5, 6, 9]


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def test_factorial():
    assert factorial(5) == 120


