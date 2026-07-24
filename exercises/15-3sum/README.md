# 3 Sum

## Problem

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 
```markdown
Example 1:


Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
```

```markdown
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
```

```markdown
Example 3:


Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
```

```markdown
Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
```


## Approach

The first possible approach is to try every combination with three nested loops, but that would take `O(n^3)` time.

But if you stop and think we are actually being asked for three numbers (well its unique combinations) that sum to 0:

```markdown
a + b + c = 0
```

But what if we do this:

```markdown
b + c = -a
```

This then becomes very simiarl to an issue we tackled before, two sum!

There are two important details: the array must be sorted so the pointers have a useful direction, and duplicate values must not produce duplicate triplets. Sorting costs `O(nlogn)`, but it lets the two-pointer search run in linear time for each anchor.

The key here then is to iterate once for every number, with a for loop, which becomes our anchor, and then we two-sum to find that anchor value:

```python

        nums.sort()
        res = []

        for i, anchor in enumerate(nums):
            # the same anchor would search the same remaining range again.
            if i > 0 and anchor == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            target = -anchor
            while left < right:
                local_total = nums[left] + nums[right]
                if local_total < target:
                    left += 1
                elif local_total > target:
                    right -= 1
                else:
                    res.append([anchor, nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # avvoid adding the same pair for this anchor twice.
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return res
```

The final implementation changes the first draft in three ways:

1. It skips duplicate anchors before starting a search.
2. It uses the sorted order to move `left` when the sum is too small and `right` when it is too large.
3. After finding a valid triplet, it moves both pointers and skips duplicate values so the result contains unique triplets without repeatedly checking `r not in res`.

## Complexity


### Time: O(n^2)

We have three main operations:

1. Sorting `O(nlogn)`
2. One for `O(n)`
3. The while which is `O(n)`

So at the end we sume as `O(nlogn) + O(n) * O(n)` so we get a `O(n^2)`.

### Space: O(1) 

Apart from the returned result, the algorithm uses a constant number of variables. The result itself requires `O(k)` space for `k` triplets. `nums.sort()` sorts in place; using `sorted(nums)` instead would avoid mutating the caller's list but would require an additional `O(n)` list.


# Learnings

- Many problems can be simplified by transforming the equation. In this case:

  ```markdown
  a + b + c = 0
  # can be written as 
  b + c = -a
  ```

  Once one value is fixed (the anchor), the problem becomes a Two Sum problem.

- Sorting is often worth the `O(nlogn)` cost because it enables efficient techniques like two pointers, reducing the overall complexity from `O(n^3)` to `O(n^2)`.

- The two-pointer search is `O(n)`, not `O(n^2)`, because each pointer only moves in one direction. Across a single search, each pointer visits each index at most once.

- A useful strategy for problems involving combinations is:
  1. Fix one element (anchor).
  2. Reduce the problem to a smaller one.
  3. Solve the reduced problem efficiently.

- Checking `r not in res` can hide duplicate-handling work and make the solution less efficient. Because the input is sorted, duplicates can be skipped while the pointers move.
