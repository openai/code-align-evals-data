# [PROMPT]


def by_length(arr):
    """
    Given an array of integers, if the number is an integer between 1 and 9 inclusive,
    replace it by its corresponding name from "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
    otherwise remove it, then sort the array and return a reverse of sorted array.

    For example:
      arr = [2, 1, 1, 4, 5, 8, 2, 3]
            -> sort arr -> [1, 1, 2, 2, 3, 4, 5, 8]
            -> reverse arr -> [8, 5, 4, 3, 2, 2, 1, 1]
      return ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]

      If the array is empty, return an empty array:
      arr = []
      return []

      If the array has any strange number ignore it:
      arr = [1, -1 , 55]
            -> sort arr -> [-1, 1, 55]
            -> reverse arr -> [55, 1, -1]
      return = ['One']
    """
    # [SOLUTION]

    dic = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
    }
    sorted_arr = sorted(arr, reverse=True)
    new_arr = []
    for var in sorted_arr:
        try:
            new_arr.append(dic[var])
        except:
            pass
    return sorted_arr


# [CHECK]
def check(candidate):

    # Check some simple cases
    assert True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate([2, 1, 1, 4, 5, 8, 2, 3]) == [
        "Eight",
        "Five",
        "Four",
        "Three",
        "Two",
        "Two",
        "One",
        "One",
    ], "Error"
    assert candidate([]) == [], "Error"
    assert candidate([1, -1, 55]) == ["One"], "Error"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"
    assert candidate([1, -1, 3, 2]) == ["Three", "Two", "One"]
    assert candidate([9, 4, 8]) == ["Nine", "Eight", "Four"]


if __name__ == "__main__":
    check(by_length)
