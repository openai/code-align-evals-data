ENTRY_POINT = 'can_arrange'
FIX = """
Fixed typo arange -> arrange
Remove semicolon from solution
"""

#[PROMPT]

def can_arrange(arr):
    """Create a function which returns the index of the element such that after 
    removing that element the remaining array is itself sorted in ascending order.
    If the given array is already sorted in ascending order then return -1.
    Note: It is guaranteed that the array arr will either be sorted or it will
          have only one element such that after its removal the given array
          will become sorted in ascending order.
          - The given array will not contain duplicate values.
    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
#[SOLUTION]
    ind=-1
    i=1
    while i<len(arr):
      if arr[i]<arr[i-1]:
        ind=i
      i+=1
    return ind
#[CHECK]
def check(candidate):

    # Check some simple cases
    assert candidate([1,2,4,3,5])==3
    assert candidate([1,2,4,5])==-1
    assert candidate([1,4,2,5,6,7,8,9,10])==2

    # Check some edge cases that are easy to work out by hand.
    assert candidate([])==-1

