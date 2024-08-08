# Hackerrank Archive

1. ## [Strings](###Strings)
1. ## [Stacks](###Stacks)
3. ## [Queues](###Queues)


### Strings

- [Anagram](https://github.com/papilo-cloud/Python_Data_Structures-/blob/main/Hackerrank/strings/anagram.py) Two words are anagrams of one another if their letters can be rearranged to form the other word.

    Given a string, split it into two contiguous substrings of equal length. Determine the minimum number of characters to change to make the two substrings into anagrams of one another.

    #### Returns
    - int: the minimum number of characters to change or -1.
- [Pangrams](https://github.com/papilo-cloud/Python_Data_Structures-/blob/main/Hackerrank/strings/pangram.py) A pangram is a string that contains every letter of the alphabet. Given a sentence determine whether it is a pangram in the English alphabet. Ignore case. Return either pangram or not pangram as appropriate.

    #### Example
    *s* = __The quick brown box jumps over the lazy dog__

    The string contains all letters in the English alphabet, so return pangram.

    #### Returns
    - It should return the string pangram if the input string is a pangram. Otherwise, it should return not pangram.


### Stack

- Implement a simple text editor. The editor initially contains an empty string, __*S*__. Perform  __*Q*__ operations of the following __4__ types:

    1. append __(*W*)__ - Append string __*W*__ to the end of __*S*__.
    delete __(*K*)__ - Delete the last __*K*__ characters of __*S*__.
    print __(*K*)__ - Print the __*K<sup>th</sup>*__ character of __*S*__.
    undo __()__ - Undo the last (not previously undone) operation of type __1__ or __2__, reverting __*S*__ to the state it was in prior to that operation.

    #### Example
    __*S*__ = __'abcde'__
    __*ops*__ = __['1 fg', '3 6', '2 5', '4', '3 7', '4', '3 4']__





