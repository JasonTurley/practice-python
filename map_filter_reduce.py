# My implementations of the map, filter, and reduce functiontions.

###############################################################################
# Custom implementations                                                      #
###############################################################################

def my_map(function, items):
    """
    Creates and returns the list created by applying the `function` to all
    `items` in the given list.
    """
    result = []

    for it in items:
        result.append(function(it))

    return result

def my_filter(condition, items):
    """
    Creates and returns a list of items for which the `condition` is true.
    """
    result = []

    for it in items:
        if condition(it):
            result.append(it)

    return result

###############################################################################
# Test Wrappers                                                               #
###############################################################################

def test_my_map(function, items):
    result = my_map(function, items)
    expected = list(map(function, items))

    assert result == expected


def test_my_filter(condition, items):
    result = my_filter(condition, items)
    expected = list(filter(condition, items))

    assert result == expected


# Add test cases here
if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6]
    nums2 = [88, -2, 0, -33, 201, -71]

    test_my_map(lambda x: x + 2, nums)
    test_my_map(lambda x: x**2, nums)

    test_my_filter(lambda n: n < 0, nums)
    test_my_filter(lambda n: n < 0, nums2)

    print("Passed all test cases.")
