"""
CMPS 6610  Assignment 1.
See problemset-01.pdf for details.
"""
# no imports needed.

def foo(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a

    x = min(a, b)
    y = max(a, b)

    return foo(x, y % x)

def longest_run(mylist, key):
    longest = 0
    current = 0

    for value in mylist:
        if value == key:
            current += 1
            longest = max(longest, current)
        else:
            current = 0

    return longest


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size              # the length of the longest run on left side of input
                                                # eg, with a key of 12, [12 12 3] has left_size of 2 
        self.right_size = right_size            # length of longest run on right side of input
                                                # eg, key 12, [3 12 12] has right_size of 2
        self.longest_size = longest_size        # length of longest run in input
                                                # eg, [12 12 4 12 12 12]: longest_size is 3
        self.is_entire_range = is_entire_range  # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    
    
def longest_run_recursive(mylist, key):
    # Base case: an empty list has no run
    if len(mylist) == 0:
        return Result(0, 0, 0, True)

    # Base case: a list with one item
    if len(mylist) == 1:
        if mylist[0] == key:
            return Result(1, 1, 1, True)
        else:
            return Result(0, 0, 0, False)

    # Split the list into two halves
    middle = len(mylist) // 2

    # Recursively solve the left and right halves
    left = longest_run_recursive(mylist[:middle], key)
    right = longest_run_recursive(mylist[middle:], key)

    # Determine the run length starting from the left edge
    if left.is_entire_range:
        left_size = left.left_size + right.left_size
    else:
        left_size = left.left_size

    # Determine the run length ending at the right edge
    if right.is_entire_range:
        right_size = right.right_size + left.right_size
    else:
        right_size = right.right_size

    # The longest run may be entirely on the left,entirely on the right, or cross the midpoint
    longest_size = max(
        left.longest_size,
        right.longest_size,
        left.right_size + right.left_size
    )

    # The entire range matches only if both halves completely match
    is_entire_range = (
        left.is_entire_range and right.is_entire_range
    )

    # Return the combined result for this section of the list
    return Result(
        left_size,
        right_size,
        longest_size,
        is_entire_range
    )