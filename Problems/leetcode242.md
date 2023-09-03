# Problem 242. Valid Anagram

## Description:

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Solution

1. Go over the first string "s", store each character in a dictionary - keep the character as the key and the count as the value
2. Go over the second string "t", this time, if decrement the count as you go along.
3. Finally, go over the dictionary and check if there are non zero values. If there are non-zero values you need to return False

``` python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            d1 = defaultdict(int)
            for i in s:
                d1[i] += 1 
            for i in t:
                d1[i] -= 1
            for val in d1.values():
                if val != 0:
                    return False

        return True

```