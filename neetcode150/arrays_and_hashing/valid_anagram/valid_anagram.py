# Problem description : https://leetcode.com/problems/valid-anagram/description/
def isAnagram(s, t) :
    # make a list and sort letters
    s_letters = sorted(list(s))
    t_letters = sorted(list(t))

    # compare the two lists
    if s_letters == t_letters:
        return True
    else :
        return False
    
# Tip : check if len(s) == len(t) before any calculation, this can save time.