"""
I was bored one day and decided to look at last names in the phonebook for my
area.

I flipped open the phonebook to a random page near the middle and started
perusing. I wrote each last name that I was unfamiliar with down on paper in
increasing order. When I got to the end of the phonebook, I was having so much
fun I decided to start from the beginning and keep going until I reached the
page where I had started.

When I was finished, I had a list of interesting last names that were mostly
alphabetical. The problem was that my list starts somehere near the middle of
the alphabet, reaches the end, and then starts from the beginning of the
alphabet. In other words, my list of names is sorted, but it is "rotated."

Example:

surnames = [
    'liu',
    'mcdowell',
    'nixon',
    'sparks',
    'zhang',
    'ahmed',  # <-- rotates here!
    'brandt',
    'davenport',
    'farley',
    'glover',
    'kennedy',
]

Write a function that finds the index of the "rotation point". The "rotation
point" is where I started working from the beginning of the phone book. The
list I came up was absolutely huge, so make sure your solution is efficient.

*Note: you should be able to come up with a solution that has O(log n) time
complexity.*
"""


def find_rotation_point(surnames: List[str]) -> int:
    # Your code here

    # Worst Case runtime is O(n) since we are doing a linear pass thorough our list of names

    # Idea 1 -> Iterate through list of names
        # Check names 2 at a time
        # If we see the second name doesn't come after the first name in alpha ordering
            # Thats our rotation point, return index
    # This plan doesn't take advantage of the fact the input is sorted

    # Idea 2 -> How can we take advantage that the data is sorted?
    # Binary search: if you're tasked with searching through sorted data, you should always consider it
    # To denote the boundaries of our search space, we'll have two variables, left and right

    left = 0
    right = len(surnames) - 1

    # loop so long as left < right
    while left < right:

        # Get the midpoint of the current search space
        mid = ((right - left) // 2) + left

        # Check the midpoint element against the first element in the search space
        # if the midpoint element is greater than the first element
        if surnames[mid] > surnames[left]:
            # Go right
            left = mid 
    
        # else 
        else:
            # Go left
            # When we go left, we can't eliminate the midpoint element itself, since it might be the rotation point
            right = mid
        # check if left and right are next to each other
        if left + 1 == right:

            # return right index
            return right
        


