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

def locate_card(cards, query):  # {always write the function signature}

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
print('answer one result is ', answer_one)


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


def locate_card(cards, query):
    def condition(mid):  # we are creating nested functions here
        if cards[mid] == query:  # this shows if the query is founded in mid-check
            if mid > 0 and cards[mid - 1] == query:  # check is mid greater than 0 or is there any same number found in
                # left side of the array
                return 'left'  # if yes check in left side in the array
            else:  # if not found then the mid is our answer so returns mid, means found
                return 'found'
        elif cards[mid] < query:
            return 'left'
        else:
            return 'right'


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


# REVISION OF BINARY SEARCH WITH PRINT STATEMENT.   DATE: 01-08-2025

def find_numbers(nums, query):  # this is our function (for better readability)
    lo, hi = 0, len(nums) - 1  # this line means we are setting two pointers which start from 0'th element and go till
    # last element means nth -1 element. We declare our position is from 0 to n-1 position this is our search space
    while lo <= hi:  # We use while loop till our search space is valid means (lo and hi are equal or less than hi)
        mid = lo + hi // 2  # we use double slash cause python automatically give decimal number which we want to avoid
        mid_number = nums[mid]

        print("lo:", lo, "hi:", hi, "mid point:", mid, "mid number:", mid_number)
        # We use print statements for easy debugging it helps to identify errors location
        if mid_number == query:
            return mid
        elif mid_number < query:
            hi = mid - 1
        else:
            lo = mid + 1
    return -1

    # THIS IS FOR FIRST OCCURRENCE OF THE QUERY IF THE QUERY REPEATS MULTIPLE TIMES  Date: 03-08-2025


def find_location(nums, query, mid):
    mid_number = nums[mid]
    print("Mid:", mid, "Mid Number:", mid_number)
    if mid_number == query:  # it checks the number is equal to query or not
        if mid - 1 >= 0 and nums[mid - 1] == query:  # We are checking the position of mid-1. Is mid-1 a valid position
            # or not. Then we check is mid-1 is equal to the query or not if yes return left cause query exist, and it's
            # not the first occurrence of the query
            return 'left'
        else:
            return 'found'
    elif mid_number < query:
        return 'left'
    else:
        return 'right'


def locate_numbers(nums, query):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        print("lo:", lo, "hi:", hi)
        mid = (lo + hi) // 2
        result = find_location(nums, query, mid)  # Here we are passing the function(find_location) in the
        # result variable and calling the functions argument and checking them with condition statement
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return -1
