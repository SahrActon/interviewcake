# Variables

my_list_of_items = [1, 2, 3, 4, 5, 16, 7, 8]

"""
This function runs in O(1)O(1) time (or "constant time") relative to its input.
The input list could be 1 item or 1,000 items, but this function would still just require one "step."
"""


def print_first_item(items):
    print(items[0])


"""
This function runs in O(n) time (or "linear time"), where nn is the number of items in the list. 
If the list has 10 items, we have to print 10 times. If it has 1,000 items, we have to print 1,000 times.
"""


def print_all_items(items):
    for item in items:
        print(item)


"""
Here we're nesting two loops. If our list has nn items, our outer loop runs nn times 
and our inner loop runs n times for each iteration of the outer loop, 
giving us n^2n total prints. Thus this function runs in O(n^2) time (or "quadratic time"). 
If the list has 10 items, we have to print 100 times. If it has 1,000 items, we have to print 1,000,000 times.
"""


def print_all_possible_ordered_pairs(items):
    for first_item in items:
        for second_item in items:
            print(first_item, second_item)


print_first_item(my_list_of_items)
print("-----")
print_all_items(my_list_of_items)
print("-----")
print_all_possible_ordered_pairs(my_list_of_items)

"""
N could be the actual input, or the size of the input
Bother of these functions have O(n) runtime, even though one takes an integer as its input and the other takes a list:
"""


def say_hi_n_item(n):
    for time in range(n):
        print("hi")


""" Defined again just for learning purposes """


def print_all_items(items):
    for item in items:
        print(item)


print("-- Defined again just for learning purposes --")
say_hi_n_item(10)
print("-----")
print_all_items(my_list_of_items)

"""
So Sometimes n is an actual number that's an input to our function,
and other times n is the number of number of items in an input list( or input map, or input object, etc).
"""

""" Drop the constants """


def print_all_items_twice(items):
    for item in items:
        print(item)

    # Once more, for luck
    for item in items:
        print(item)


print("-- Drop the constants --")
print_all_items_twice(my_list_of_items)
print("-----")

"""
This is O(1 + n/2 + 100), which we just call O(n).

Why can we get away with this? Remember, for big O notation we're looking at what happens as n gets arbitrarily large.
As n gets really big, adding 100 or dividing by 2 has a decreasingly significant effect.
"""


def print_first_item_then_first_half_then_say_hi_100_times(items):
    print(items[0])

    middle_index = len(items) / 2
    index = 0

    while index < middle_index:
        print(items[index])
        index += 1

    for time in range(100):
        print("hi")


print("-- print_first_item_then_first_half_then_say_hi_100_times --")
print_first_item_then_first_half_then_say_hi_100_times(my_list_of_items)
print("-----")

"""
Here our runtime is O(n + n^2), which we just call O(n^2) Even if it was O(n^2/2 + 100n), it would still be O(n^2)
Similarly:

O(n^3 + 50n^2 + 10000)) is O(n^3)
O((n + 30) * (n + 5)) is O(n^2)
Again, we can get away with this because the less significant terms quickly become, well, less significant as n gets big.

"""

print("-- Drop the less significant terms --")


def print_all_numbers_then_all_pair_sum(numbers):
    print("these are the numbers")
    for number in numbers:
        print(number)

    print("add these are their sums")
    for first_number in numbers:
        for second_number in numbers:
            print(first_number + second_number)


print_all_numbers_then_all_pair_sum(my_list_of_items)

"""
Often this "worst case" stipulation is implied. But sometimes you can impress your interviewer by saying it explicitly.
Sometimes the worst case runtime is significantly worse than the best case runtime:

Here we might have 100 items in our haystack, but the first item might be the needle, i
n which case we would return in just 1 iteration of our loop.

In general we'd say this is O(n) runtime and the "worst case" part would be implied. 
But to be more specific we could say this is worst case O(n) and best case O(1) runtime. 
For some algorithms we can also make rigorous statements about the "average case" runtime.


"""
# We're usually talking about the "worst case"
print("-- We're usually talking about the 'worst case' --")


def contains(haystack, needle):
    # Does the haystack contain a needle?
    for item in haystack:
        if item == needle:
            print("Found", needle)
            return True

    print("We did not find ", needle)
    return False


print("-- Contains --")
contains(my_list_of_items, 2)

# Space complexity: the final frontier
"""
Sometimes we want to optimize for using less memory instead of (or in addition to) using less time. 
Talking about memory cost (or "space complexity") is very similar to talking about time cost. 
We simply look at the total size (relative to the size of the input) of any new variables we're allocating.
"""

# This function takes O(1) space (we use a fixed number of variables):

print("# Space complexity: the final frontier")


def say_hi_n_times(n):
    for time in range(n):
        print("hi")


say_hi_n_times(10)


# This function takes O(n)O(n) space (the size of hi_list scales with the size of the input):
def list_of_hi_n_times(n):
    hi_list = []
    for time in range(n):
        hi_list.append("hi")

    print(hi_list)
    return hi_list


print(" list of hi n times ")
list_of_hi_n_times(10)

print(" get_largeat_item ")


def get_largeat_item(items):
    largest = float('-inf')
    for item in items:
        if item > largest:
            largest = item

    print(largest)
    return largest


get_largeat_item(my_list_of_items)
