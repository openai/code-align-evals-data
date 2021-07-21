# [PROMPT]


def check_dict_case(dict):
    """
    Given a dictionary, return True if all keys are strings in lower
    case or all keys are strings in upper case, else return False.
    The function should return False is the given dictionary is empty.
    Examples:
    check_dict_case({"a":"apple", "b":"banana"}) should return True.
    check_dict_case({"a":"apple", "A":"banana", "B":"banana"}) should return False.
    check_dict_case({"a":"apple", 8:"banana", "a":"apple"}) should return False.
    check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}) should return False.
    check_dict_case({"STATE":"NC", "ZIP":"12345" }) should return True.
    """
    # [SOLUTION]

    if len(dict.keys()) == 0:
        return False
    else:
        state = "start"
        for key in dict.keys():

            if isinstance(key, str) == False:
                state = "mixed"
            if state == "start":
                if key.isupper():
                    state = "upper"
                elif key.islower():
                    state = "lower"
            elif (state == "upper" and not key.isupper()) or (
                state == "lower" and not key.islower()
            ):
                state = "mixed"
        return state == "upper" or state == "lower"


# [CHECK]
def check(candidate):

    # Check some simple cases
    assert candidate({"a": "apple", "b": "banana"}) == True, "First test error: " + str(
        candidate({"a": "apple", "b": "banana"})
    )
    assert (
        candidate({"a": "apple", "A": "banana", "B": "banana"}) == False
    ), "Second test error: " + str(
        candidate({"a": "apple", "A": "banana", "B": "banana"})
    )
    assert (
        candidate({"a": "apple", 8: "banana", "a": "apple"}) == False
    ), "Third test error: " + str(candidate({"a": "apple", 8: "banana", "a": "apple"}))
    assert (
        candidate({"Name": "John", "Age": "36", "City": "Houston"}) == False
    ), "Fourth test error: " + str(
        candidate({"Name": "John", "Age": "36", "City": "Houston"})
    )
    assert (
        candidate({"STATE": "NC", "ZIP": "12345"}) == True
    ), "Fifth test error: " + str(candidate({"STATE": "NC", "ZIP": "12345"}))
    assert (
        candidate({"fruit": "Orange", "taste": "Sweet"}) == True
    ), "Sixth test error: " + str(candidate({"fruit": "Orange", "taste": "Sweet"}))
    assert (
        candidate({"Fruit": "Orange", "taste": "Sweet"}) == False
    ), "Seventh test error: " + str(candidate({"fruit": "Orange", "Taste": "Sweet"}))

    # Check some edge cases that are easy to work out by hand.
    assert candidate({}) == False, "1st edge test error: " + str(candidate({}))


if __name__ == "__main__":
    check(check_dict_case)
