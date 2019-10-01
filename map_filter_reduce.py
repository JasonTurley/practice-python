# My implementations of the map, filter, and reduce functions.

###############################################################################
# Custom implementations                                                      #
###############################################################################

def my_map(func, items : list) -> list:
    """
    Creates a new list by applies a function `func` to all `items` in a list,
    and returns a new list.
    """
    result = []

    for it in items:
        result.append(func(it))

    return result

###############################################################################
# Test Wrappers                                                               #
###############################################################################

def test_my_map(func, items):
    result = my_map(func, items)
    expected = list(map(func, items))

    assert(result == expected)

###############################################################################
# Functions                                                                   #
###############################################################################
def plus2(x : int) -> int:
    return x + 2


if __name__ == "__main__":
    # Add test cases here
    nums = [1, 2, 3, 4, 5, 6]

    test_my_map(plus2, nums)
    test_my_map(lambda x: x**2, nums)

    print("Passed all test cases.")
