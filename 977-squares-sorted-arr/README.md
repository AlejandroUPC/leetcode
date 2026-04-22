# Squares of a Sorted Array 

## Problem

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:

```markdown
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
```

Example 2:

```markdown
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
```

## Approach

This can be returned as a sorted list of reach values, quite easy and is probably `O(n)` + the sorting probably `O(nlogn)`., only concer here is because we are generating a new list space is `O(n)` and w/ two pointers we can keep it `O(1)`?
## Complexity


### Time: O(nlogn)

So since we just iterate once over the array + sort its `O(nlogn)`.

### Space: O(n)

We generate a new list after the sorting, so `O(n)`.

## Learnings


This took me a while to figure, but felt so dumb afterwards. Given that the array is sorted, even if it contains negatives, it means that as we move across the items with two pointers on opposite directions the highest values (again squared, so negative does not matter) will be at the edges.

Imagine we have the array `[-7, 3, -1, 2, 8]` and we square it `[49, 9, 1, 4, 64]`. Where are the biggest pairs of values? at the edges as we progress until we are in the middle or pointers are about to meet.So instead of computing everything and sort, we can pick the largest square directly.

I still struggle some how to see the adventages/shortpaths of the problem ot make it tricky and get confused with points (e.g missing computing one element because of left/right boundaries check).
