import data
from typing import Optional

# Write your functions for each part in the space below.

# Part 0

# Finds the index of the smallest value in the list, if there are values,
#     starting from the provided index (if in bounds).
# input: a list of integers
# input: a starting index
# returns: index of smallest value as an int or None if no value is found
def index_smallest_from(values:list[int], start:int) -> Optional[int]:
    if start >= len(values) or start < 0:
        return None

    mindex = start
    for idx in range(start + 1, len(values)):
        if values[idx] < values[mindex]:
            mindex = idx

    return mindex


# Sorts, in place, the elements of a list using the selection sort algorithm.
# input: a list of integers
# returns: nothing is returned; the list is sorted in place
#    <This function modifies/mutates the input list. Though a traditional
#     approach, cloning the list sorting the clone is potentially less
#     surprising. Or even using a different sorting algorithm.>
def selection_sort(values:list[int]) -> None:
    for idx in range(len(values) - 1):
        mindex = index_smallest_from(values, idx)
        tmp = values[mindex]
        values[mindex] = values[idx]
        values[idx] = tmp


# Part 1
#Takes a list of data.Book type as input
#Returns nothing
#Function uses selection sort to sort the books by their title
#all within the same list
def selection_sort_books(arr: list[data.Book]) -> None:
    #Selection Sort for arr
    for idx in range(len(arr) - 1):
        mindx = idx
        for i in range(idx, len(arr)):
            if arr[i].title < arr[mindx].title:
                mindx = i

        temp = arr[mindx]
        arr[mindx] = arr[idx]
        arr[idx] = temp

# Part 2
#Takes string as input
#Returns similar string, but the case of each of the letters are flipped
def swap_case(s: str) -> str:

    x = str()

    for i in s:
        if i.isalpha():
            if i.isupper():
                x += i.lower()
            else:
                x += i.upper()
        else:
            x += i

    return x

# Part 3
#Takes a string, and two characters as input
#Returns similar string as input, but with each instance of first character
#replaced with the other
def str_translate(s: str, c1: str, c2: str) -> str:
    x = str()

    for i in s:
        if i == c1:
            x += c2
        else:
            x += i

    return x

# Part 4
#Takes string as input, splits it to words storing them in list
#returns a dictionary containing count of each of the words
#Capitalization/Case does not matter
def histogram(s: str) -> dict:
    l = s.split(' ')
    hist = dict()

    for i in l:
        i = i.lower()

        if i not in hist:
            hist[i] = 0

        hist[i] += 1

    return hist