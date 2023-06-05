
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