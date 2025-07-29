""""
 leetCode problem 702 {Binary Search}
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
