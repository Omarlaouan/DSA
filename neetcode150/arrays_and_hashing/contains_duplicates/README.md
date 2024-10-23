### Problem description
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true

Example 2:

Input: nums = [1,2,3,4]
Output: false


### Time Complexity:
The function `containsDuplicate(nums)` checks for duplicates using a set. Let's break it down:

1. **Iteration over the list (`for n in nums`)**: The loop runs once for each element in `nums`, so this is O(n), where n is the number of elements in the list.

2. **Checking membership in a set (`if n in seen`)**: Checking for membership in a set is O(1) on average, due to the underlying hash table implementation.

3. **Inserting an element into the set (`seen.add(n)`)**: Insertion into a set is also O(1) on average.

Thus, the overall time complexity is:
- **O(n)** because each element is processed once (inserted and checked).

### Memory Complexity:
The memory complexity depends on the size of the `seen` set:

- **Set `seen`**: In the worst case (when there are no duplicates), the set will store every element of `nums`. This requires O(n) additional space where n is the number of elements in the list.

Thus, the memory complexity is:
- **O(n)** due to the space required to store the elements in the set.

### Summary:
- **Time Complexity**: O(n)
- **Space Complexity**: O(n)