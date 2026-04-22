# Two Sum II - Input Array Is Sorted

## Problem


Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers `[index1]` and numbers `[index2]` where `1 <= index1 < index2 <= numbers.length`.

Return the indices of the two numbers index1 and index2, each incremented by one, as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

 

Example 1:

```markdown
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
```

Example 2:

```markdown
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
```

Example 3:

```markdown
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
```

## Approach

This seems quite straight-forward if we want to brutte force it to `O(n^2)` as:

```python
def solution(numbers: list[int], target: int) -> list[int]:
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]

```

This passes the test in LC and submission fails at tim exceeded... Yeah you can do two pointers for this (see [learnings](#Learnings))

## Complexity

### Time: O(n^2)

We go first array at least for each `i`, `j` runs `n - i - 1` and `i` runs `n`:

- Again `j` starts from `1` instead of `0` (no sense to sum indexes 0 and 0), so `n - 1` and then it shrinks on every `i`.

### Space: O(1)

No additional variables

## Learnings

This is a clear example of two pointers where basically we can start `left` and `right` (why opposite instead of same?, well because we an discriminate as explained above) and we keep iterating, the main adventage here and why this makes sense is that based on the value of the sum (are we above or below?) we can decide which pointer to move, runs on `O(n)`:

```python
def solution_2(numbers: list[int], target: int) -> list[int]:
    left = 0
    right = len(numbers) - 1
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum > target:
            right -= 1
        else:
            left += 1
```
