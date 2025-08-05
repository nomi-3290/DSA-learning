# LeetCode problem 702 {Binary Search}
""""
 Problem level: Easy
 Abstract: given an integer array which is sorted in ascending order need to find target from nums if its exist
 return its index otherwise return -1 {run time complexity 0(log n)}

 """


def binary_search(lo, hi, condition):
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return -1


def find_target(nums, target):
    def condition(mid):
        if nums[mid] == target:
            return 'found'
        elif nums[mid] < target:
            return 'right'
        else:
            return 'left'

    return binary_search(0, len(nums) - 1, condition)


"""
I broke the binary search into two functions — binary_search and find_target — just to keep it clean and reusable. 
binary_search does the usual loop stuff, and find_target just tells it when we’ve found the target or which side to 
move. This way I can easily tweak it later for things like first/last occurrence, rotated arrays, 
or any advanced version of binary search.
And yeah, it's still O(log n) — fast and clean.
"""

#  LeetCode Problem: 35 { Search Insert Position }   Date: 04-08-2025

"""
 Difficulty level: Easy     
 
 Abstract: We have to find the target if it's available in the array. The array is distinct. If not we have to  
 calculate the correct position in sorted order of the target. And return the index where it would be if it were 
 inserted in order.  
 runtime complexity 0(log n)
 
"""


def b_s(lo, hi, condition):  # b_s = for binary search write just for better understanding and memorizing while solving
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return lo


def searching_insert(nums, target):
    def condition(mid):
        if nums[mid] == target:
            return 'found'
        elif nums[mid] < target:
            return 'left'
        else:
            return 'right'
    return b_s(0, len(nums) - 1, condition)


"""
    Here our b_s function is a generic Binary Search function which compare the conditions and find the midpoint of the
    array and controls while loop. The second function Searching_insertion compare all the elements and checked if it's 
    available in the array and if not then our generic function return the lo position of the array which is the right 
    index of the given target. How so the Binary Search counts the index and divide it with and return the integer value
    and compare with mid if it's small go towards right and compare it's big the answer is MIDPOINT.
"""