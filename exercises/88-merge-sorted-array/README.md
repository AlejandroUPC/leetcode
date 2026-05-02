# Merge Sorted Array 

## Problem

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

Example 1:

```
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
```

Example 2:

```
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
```

Example 3:

```
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
```

## Approach


**Disclaimer** this span over mutliple days, so notes might be shitty, but basically if we know that a part of nums1 is going to be just `0`s lets just mix all in one array and sort it? Again using built ins so by far from ideal, then again because its must modify `nums1` in place we just iterate over the sorted array and assign the values to `nums1`:

This is how I did solution 1.


## Complexity


### Time: O((m+n) + log(m+n))

We are picking valid nums as `m` (which is the half array) and then we concat with the array `n` so `O(m+n)`, and then we sort those two so its `O(log m + n)`, so its `O((m+n) + log(n+m))`

### Space: O(m+n)

Space is also whatever the merged variable `merged` takes which is `O(m+n)`.

## Learnings


This was by far a bit hard to tackle because was distracted, but you can there are some great insights I found out:

1. We start filling from right, because its the safest.
2. If we start filling `nums1` from right, so replacing the 0's we also need to iterate both arrays from the right.
3. We obviously need two pointers, starting from right, and whenever we find the biggest number we move the pointer to the left.
4. We are done when we consume all of the `nums2` array, meaning that we have positioned all of its values (if they were all bigger on the `0`s) or we can add those values at the start of `nums1`.

This improves time to `O(m+n)` and space to `O(1)`.
