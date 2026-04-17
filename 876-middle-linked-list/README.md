# Middle of The Linked List

Disclaimer, lost all the changes I had for this one, sorry, most of the content will be in main.py then, tldr is two times iteration, one full one until half or fast/slow pointer.
## Problem

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:

Input: head = [1,2,3,4,5]

Output: [3,4,5]

Explanation: The middle node of the list is node 3.


Example 2:

Input: head = [1,2,3,4,5,6]

Output: [4,5,6]

Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.


## Approach

Use two pointers:

- `slow` moves 1 step at a time
- `fast` moves 2 steps at a time

When `fast` reaches the end, `slow` is at the middle. For even-length lists, this returns the second middle node.

## Complexity
- Time: O(n)
- Space: O(1)
