# Problem 92: Reverse Linked List II
## Difficulty: Medium

## Statement:
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.


## Solutions (Python):

- Essentially we are rotating the linkedlist "counter-clockwise"

```python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if (left == right):
            return head
        dummy = ListNode(0, head)

        previous = dummy
        for i in range(left-1):
            previous = previous.next
        current = previous.next
        # This loop reverses the 
        for i in range (right - left):
            forward = current.next
            current.next = forward.next
            forward.next = previous.next
            previous.next = forward
        return dummy.next

                        
```

🔖 [Leetcode #75](https://leetcode.com/problems/sort-colors/description/)
🔖 [Dutch National Flag Approach](https://leetcode.com/problems/sort-colors/solutions/3464652/beats-100-c-java-python-javascript-two-pointer-dutch-national-flag-algorithm/)