"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4

def sublist(A, B):
    if A == B:
        return EQUAL
    if not A:
        return SUBLIST
    if not B:
        return SUPERLIST
    len_a = len(A)
    len_b = len(B)
    for i in range(len_b - len_a + 1):
        if B[i:i+len_a] == A:
            return SUBLIST
    for i in range(len_a - len_b + 1):
        if A[i:i+len_b] == B:
            return SUPERLIST
    return UNEQUAL