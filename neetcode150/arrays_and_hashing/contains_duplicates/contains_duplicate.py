# Problem description : https://leetcode.com/problems/contains-duplicate/description/
def containsDuplicate(nums):
    seen = set()  # Set to track seen numbers
    for n in nums:
        if n in seen:  # If n is already in the set, there's a duplicate
            return True
        seen.add(n)  # Add n to the set if it's not seen before
    return False  # No duplicates found

# Testing 
nums = [1, 2, 3, 1]
print(containsDuplicate(nums))