# Uses python3
import sys

def binary_search(a, x):
    left, right = 0, len(a)
    while left <= right:
        mid = (right - left)//2 + 1
        if a[mid] == x:
            return mid
        if a[mid] < x:
            left += mid
            continue
        if a[mid] > x:
            right -= mid
            continue
    return -1
