# Maximize Expression of Three Elements 

## Problem

You are given an integer array nums.

Choose three elements a, b, and c from nums at distinct indices such that the value of the expression a + b - c is maximized.

Return an integer denoting the maximum possible value of this expression.

 

Example 1:

Input: nums = [1,4,2,5]

Output: 8

Explanation:

We can choose a = 4, b = 5, and c = 1. The expression value is 4 + 5 - 1 = 8, which is the maximum possible.

Example 2:

Input: nums = [-2,0,5,-2,4]

Output: 11

Explanation:

We can choose a = 5, b = 4, and c = -2. The expression value is 5 + 4 - (-2) = 11, which is the maximum possible.


## Approach

Might be wrong but this seems to be an approach where just want to add the two biggest numbers in an array, add them, and take off the smallest one (even if < 0), so we obtain the highest number possible?

Again, kind of a brutte force solution but I expect to be humbled soon agian, this passes the two tests:

```python
def solution(nums: list[int]) -> int:
    smallest: int = 101
    biggest = [-101]
    for n in nums:
        if n < smallest:
            smallest = n
        if n > min(biggest):
            biggest = [n, max(biggest)]
    return sum(biggest) - smallest
```

But there is probably a much smarter way to go about it, also don't like using the values in smallest/biggest as placeholders based on the problem constraints.
LC submission is bad, betas only 7.33% on rutneim but at leasdt 89.56% in mem.
## Complexity


### Time: O(n)

We iterate once for on the array to compute, so its depending on the array's size `O(n)`.

### Space: O(1)

We declare just a varible which is an array of two items and just the small, `O(1)`.

## Learnings


Actually the solution was kinda okish after LLMing and checking around a bit, based on the optimal solution.

The approach is right, which is quite straight forward, now the solution could be more elegant:

```python
def solution_2(nums: list[int]) -> int:
    min1 = float("inf")
    max1 = max2 = float("-inf")  # max 1 is the largets, max 2 second largest
    for n in nums:
        if n < min1:
            min1 = n
        if n > max1:  # if the biggest number we've
            max2 = max1  # prev biggest is second biggest
            max1 = n  # reassign biggest
        elif n > max2:  # if its only biggest to the second, then
            max2 = n
    return max1 + max2 - min1
```

Performs slightly better and I like the handling of max values.