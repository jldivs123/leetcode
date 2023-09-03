# Problem 217: Contains Duplicate

## Description: 
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

## Solution 

Iterate through the array, check if the current item exists on a hashmap

If it exist:
  return True
Otherwise:
  store it on the hashmap

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dictionary = {}
        for num in nums:
            if num not in dictionary:
                dictionary[num] = True
            else:
                return True
        return False
```
