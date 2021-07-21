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
    
    Example solution:
    # line 1
    if len(dict.keys()) == 0:
        # line 2
        return False
    # line 3
    else:
        # line 4
        state = "start"
        # line 5
        for key in dict.keys():
            # line 6
            if isinstance(key, str) == False:
                # line 7
                state = "mixed"
                # line 8
                break
            # line 9
            if state == "start":
                # line 10
                if key.isupper():
                    # line 11
                    state = "upper"
                # line 12
                elif key.islower():
                    # line 13
                    state = "lower"
                # line 14
                else:
                    # line 15
                    break
            # line 16
            elif (state == "upper" and not key.isupper()) or (
                state == "lower" and not key.islower()
            ):
                # line 17
                state = "mixed"
                # line 18
                break
            # line 19
            else:
                # line 20
                break
        # line 21
        return state == "upper" and state == "lower"
        
    """
    # Please print out which line of the above program contains an error. E.g. if the bug is on line 4 then print 4
    # END OF CONTEXT
    print("21")
    # END OF SOLUTION


def check(candidate):

    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        candidate({})
    out = f.getvalue().strip('\n')
    assert "21" == out
    for i in range(0, 25):
        if i != 21:
            assert str(i) != out

if __name__ == "__main__":
    check(check_dict_case)
