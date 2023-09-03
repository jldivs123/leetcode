# Problem 49 Group Anagrams

## Description

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Solution
1. Iterate over the words in the input `strs`
2. Sort out the characters with `sorted()` function then make it a string using `''.join(sorted(word))` expression
3. Store them in a map (or even a hashmap) as an array/list of strings (append every word) you go encounter to its respective key

``` python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = defaultdict(list)
        for word in strs:
            sorted_word = ''.join(sorted(word))
            answer[sorted_word].append(word)
        return list(answer.values())
```