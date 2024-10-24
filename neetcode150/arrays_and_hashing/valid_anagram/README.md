### Problem description
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false

 

### Time Complexity:
The function `isAnagram(s, t)` checks if two strings are anagrams by sorting their characters. Let's break it down:

1. **Converting the strings to lists (`list(s)` and `list(t)`)**: This operation takes O(n) for both strings, where n is the length of each string (assuming both strings are of the same length). 

2. **Sorting the lists (`sorted(list(s))` and `sorted(list(t))`)**: Sorting takes O(n log n) time for each list. Since we are sorting both strings, this is done twice.

3. **Comparing the sorted lists (`if s_letters == t_letters`)**: Comparing two lists element by element takes O(n) time.

Thus, the overall time complexity is:
- **O(n log n)** because sorting is the dominant operation, and it is applied to both strings.

### Memory Complexity:
The memory complexity depends on the space used to store the sorted lists:

- **Space for sorted lists**: We are creating new lists to store the sorted characters of both `s` and `t`, which takes O(n) space for each list.

Thus, the memory complexity is:
- **O(n)** due to the additional space used for sorting.

### Summary:
- **Time Complexity**: O(n log n)
- **Space Complexity**: O(n)