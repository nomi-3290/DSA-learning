# STEPS TO HANDLE CODING PROBLEMS
# 1) State the problem clearly. Identify the input and output formats.
# 2) Come-up with some example input and outputs. Try to cover all edge cases.

# Tips name the function appropriately and think carefully about the signature.
# Use descriptive variable name either we can forget what a variable represent.

# Test cases
# 1) the query occurs somewhere middle of the list
# 2) query is the first element
# 3) query is the last element
# 4) the list contain only one element which is query
# 5) the list does not contain number query
# 6) the list is empty
# 7) the list contain repeating number
# 8) the number query occurs at more than one position in list
# 9) Maybe more

#
# simple solution of the question.

# BRUTE FORCE ALGORITHM

# in this we go in line or start from index one or go till the last one and compare the output

"""def locate_card(cards, query):  # {always write the function signature}

    position = 0
    while position < len(cards):
        if cards[position] == query:
            return position

        position += 1
        if position == len(cards):
            print('ERROR 404')
            return -1


cards_list = []  # not found in the array or empty array
query_find = 65
answer = locate_card(cards_list, query_find)
print('Answer', answer)

list_one = [1, 2, 32, 45, 55, 66, 88, 2, 3, 8, 9, 4, 5, 6, 4, 1, 22]
query_one = 1
answer_one = locate_card(list_one, query_one)
print('answer one result is ', answer_one')"""


# now we have to make this solution optimal cause it constrains that we have to pick the wanted card in the least
# amount of tries.
# { When ever we see the sorted array, and we know its in sorted order and,
# we have to compare the array and find the solution we always use the BINARY SEARCH }

# THE GENERIC CODE OF BINARY SEARCH ALGORITHM

def binary_search(lo, hi, condition):
    while lo <= hi:  # putting while loop for checking and breaking the condition
        mid = (lo + hi) // 2  # finding mid by dividing it by 2 and converting it into an integer
        result = condition(mid)  # passing middle value from condition and storing in result
        if result == 'found':  # if result matches the condition
            return mid  # returning mid as an answer cause it matches the condition
        elif result == 'left':  # if not we are going to the left side of the array
            hi = mid - 1  # mid -1 means left side of the array and setting hi is to left of half of the array
        else:  # if the condition not found in left we dig in into the right side of the for search
            lo = mid + 1  # we are setting the lo to search in right side half of the array
    return -1  # if the condition is not found and while loop ends then we return -1 (empty array, not found)


'''def locate_card(cards, query):
    def condition(mid):  # we are creating nested functions here
        if cards[mid] == query:  #  this shows if the query is founded in mid check
            if mid > 0 and cards[mid - 1] == query:  # check is mid greater than 0 or is there any same number found in 
            #right side of the array
                return 'left'  # if yes check in left side in the array
            else: # if not found then the mid is our answer so return the mid, means found
                return 'found'
        elif cards[mid] < query:
            return 'left'
        else:
            return 'right'''
# leetCode problem 34 solution find the first and last position of the given number from the given array


def first_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid > 0 and nums[mid-1] == target:
                return 'left'
            return 'found'
        elif nums[mid] < target:
            return 'right'
        else:
            return 'left'
    return binary_search(0, len(nums-1), condition)


def last_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid < len(nums) - 1 and nums[mid + 1] == target:
                return 'right'
            return 'found'
        elif nums[mid] < target:
            return 'right'
        else:
            return 'left'
    return binary_search(0, len(nums)-1, condition)


def first_and_last_position(nums, target):
    return first_position(nums, target), last_position(nums, target)
