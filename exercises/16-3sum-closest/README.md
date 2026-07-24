# 3 Sum Closest

## Problem

Given an integer array nums of length n and an integer target, find three integers at distinct indices in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 
```markdown
Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
```

```markdown
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
```


## Approach

Very similar to the three sum, the only difference here is that we have a requisite to keep the closest value after summing the three numbers and comparing it to the target.

Regardless of this I did some mistake, like using the distance (which does `abs`) to compute which pointer to move (made no sense it, by doing abs we were eliminating the direction (positive or negative) and some edge cases failed).

The idea here is then:

1. Sort input `O(nlogn)`.
2. Do a three sum `O(n^2)`.
3. For every three sum iteration, compute the distance, if its smaller you keep the current sum. The distance is only used to compare how close the candidate is, not to move the pointers.
4. Standard two pointer, if our current sum is still smaller than the target we move the pointer to get a bigger number (`left += 1`), else we move the other pointer to get a smaller number (`right -= 1`).

The important distinction here is that the distance tells us if we found a better answer, but the current sum compared to the target tells us which pointer to move.


```python
import math
def solution(nums: list[int], target: int) -> int:
    nums.sort()
    min_dist = math.inf
    res = 0
    for i in range(0, len(nums)):
        left = i + 1
        right = len(nums) - 1
        while left < right:
            current_sum = nums[left] + nums[i] + nums[right]
            current_dist = abs(target - current_sum)
            if current_dist < min_dist:
                min_dist = current_dist
                res = current_sum
            if current_sum == target:
                return current_sum
            elif current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
    return res

```

## Complexity


### Time: O(n^2)

Same as a three sum, sorting is `O(nlogn)` and then we have the for loop for `O(n)` and the standard `O(n)` from the three sum pointer movement, `O(nlogn) + O(n) * O(n) = O(n^2)`.

### Space: O(1)

Constant, we modify the array in place and the variables are created regardless of the size.

## Learnings

A bit of learnings here, again two pointer being relative simply I tend to mess up to what to look to decide when to move the pointer, I feel this was very similar (other than keeping the state of closer dist), slowly feeling comfortable but still making stupid mistakes.

The main mistake was using the distance to decide which pointer to move. The distance uses `abs`, so it removes whether we are above or below the target. It is useful to compare candidates, but to move the pointers we need to compare the actual `current_sum` with the target:

- if `current_sum < target`, we need a bigger sum, so we move `left`;
- if `current_sum > target`, we need a smaller sum, so we move `right`.
