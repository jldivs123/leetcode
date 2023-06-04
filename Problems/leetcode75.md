# Problem 74: Sort Colors

## Statement:
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.



## Solutions (Python):

1. Using bubble sort

```python

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            swapped = False
            # Why `len(array) - i - 1`?
            # Because, using bubble sort, every iteration we put the highest value to the last place
            # Hence, we don't need to compare to succeeding iteration
            for j in range(0, len(nums) - i - 1):
                if (j < len(nums) - 1):
                    if(nums[j] > nums[j + 1]):
                        temp = nums[j]
                        nums[j] = nums[j + 1]
                        nums[j + 1] = temp
                        swapped = True
            if swapped == False:
                break
        return nums

                        
```

🔖 [Leetcode #75](https://leetcode.com/problems/sort-colors/description/)
🔖 [Dutch National Flag Approach](https://leetcode.com/problems/sort-colors/solutions/3464652/beats-100-c-java-python-javascript-two-pointer-dutch-national-flag-algorithm/)