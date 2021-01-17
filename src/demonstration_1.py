"""
Given an array of integers `nums`, define a function that returns the "pivot" index of the array.

The "pivot" index is where the sum of all the numbers on the left of that index is equal to the sum of all the numbers on the right of that index.

If the input array does not have a "pivot" index, then the function should return `-1`. If there are more than one "pivot" indexes, then you should return the left-most "pivot" index.

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The sum of the numbers to the left of index 3 (1 + 7 + 3 = 11) is equal to the sum of numbers to the right of index 3 (5 + 6 = 11).
Also, 3 is the first index where this occurs.

Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
"""


def pivot_index_old(nums):  # O(n^2)
    for index, each in enumerate(nums):     # O(n)
        right_val = sum(nums[index + 1:])   # O(n/2)
        left_val = sum(nums[:index])        # O(n/2)
        if left_val == right_val:
            return index
    return -1


def pivot_index_left_right(nums):  # O(n)
    l_sum = 0
    r_sum = sum(nums[1:])
    for index in range(len(nums)):
        if l_sum == r_sum:
            return index
        l_sum += nums[index]
        if (index + 1 == len(nums)):
            r_sum = 0
        else:
            r_sum -= nums[index+1]
    return -1


def pivot_index(nums):  # O(n)
    total_sum = sum(nums)
    left_sum = 0
    for index in range(len(nums)):
        right_sum = total_sum - left_sum - nums[index]
        if left_sum == right_sum:
            return index
        left_sum += nums[index]
    return -1


print(pivot_index([1, 7, 3, 6, 5, 6]))
print(pivot_index([1, 2, 3]))
