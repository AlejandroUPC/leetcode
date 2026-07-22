# Title

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
Describe the problem here.
```


## Approach

One of the first approaches (and not effective) could be do all the combinations, or a triple nested loop that would lead to `O(n^3)`.

But if you stop and think we are actually being asked for three numbers (well its unique combinations) that sum to 0:

```markdown
a + b + c = 0
```

But what if we do this:

```markdown
b + c = -a
```

This then becomes very simiarl to an issue we tackled before, two sum!

There are some caveats here, the array has to be sorted so (and because this is a two pointer check) so we are adding some overhead, but then we can do two sum which is `O(n)`.

The key here then is to iterate once for every number, with a for loop, which becomes our anchor, and then we two-sum to find that anchor value:

```python

        nums.sort()
        res = []
        for i, anchor in enumerate(nums):
            target = -anchor
            right = len(nums) - 1
            left = i + 1
            while left < right:
                local_total = nums[left] + nums[right]
                if local_total > target:
                    right -= 1
                elif local_total < target:
                    left += 1
                elif local_total == target:
                    r = [nums[left], anchor, nums[right]]
                    left += 1
                    right -= 1
                    if r not in res:
                        res.append(r)
        return res
```

## Complexity


### Time: O(n^2)

We have three main operations:

1. Sorting `O(nlogn)`
2. One for `O(n)`
3. The while which is `O(n)`

So at the end we sume as `O(nlogn) + O(n) * O(n)` so we get a `O(n^2)`.

### Space: O(1)

Same number of variables regardless of input.


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
