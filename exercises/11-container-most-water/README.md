# Container With Most Water


## Problem

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 
```markdown
Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
```

```markdown
Example 2:
Input: height = [1,1]
Output: 1
 ```


## Approach

Spent a good amount of time understanding this, basically maybe because of the break but basically we are looking at an optimization problem for the area.
If you imagine just some lines that represent water (e.g a bar graph) and we work in two axies `x` and `y` we want:

1. Try to pick the biggest (to get a wider area) `x` possible to increase the area.
2. Pick the highest `y` (constraints the height of the rectangle).

So we have to optimize for those two things, again its important to remember that the value of `x` ha to be the broadest possible and `y` should be the one that leaves less bars cut from the top, or to be clearer maximize the product (area) limiting the height as little as possible.

Again here the graph is very useful:

![question 11](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg)


**DISCLAIMER** came back after a while, following up with notes here so afetr investigating a bit, it seems that when declaring two pointers, one left and one right, moving the next pointer to a lower (not so tall) line will screw us over, as the area will be always smaller (again the smallest height decides the entire height of the container), so the check ends up being quite easy, we simply check if the next line, both left and right, is smaller if the current, if it is then we dont move, otherwise we move.

The first function `solution` passes the tests and when submitting failed in some cases like input `[1, 2, 1]` should return `2` so I guess I am missing a single line container, added a hacky check but next test failed so I moved into `solution2` with the help of LLM explanation.

## Complexity


### Time: O(n)

Run time is `O(n)`, worst case scenario we increase with the array size.

### Space: O(1)

Space is `O(1)`, constant regardless of the size input.

## Learnings


Apparently there is plenty of wrong, the first issue is that we return early after checking just one case, when we can't find that both, for left and right the next values are smaller than our current one, so if we dont see an improevemnt we stop. **The best answer is not necessarely the first valid pair**, 

Aditionally one of our point is, move only if next item is taller, again, we are not just focusing in this solution to keep increasing the height but about eliminating impossible candidates, for example:

```markdown
height = [7, 1, 7, 7]
left=0 (7) and next_left=1(1) -> not taller, we stay
right=3 (7), next_right=2 (7) -> equal, dont move
we return area inmediately
```

We should keep a counter of the area and return the best result as we iterate.

The next_left/next_right is quite stupid (lol for real) when you check it, doing `max(a+1, a)` will always be `a+1` and similar with `min`.
The final hack we did also to pass one of the test is also wrong `left == right` given that we can't form a single container line.

Step by step we should think of checking all the candidates and picking the best one:

1. What defines a candidate? Any pair (left, right)
2. Do we need to check more than one pair? Yes
3. What are we optimizing for? area

So the question is, how do we systemically explore candidates without checking all pairs on `O(n^2)`?

The new approach is then:

1. At every step, we have a tuple `(left, right)`, with an `area = width * min(height[left], height[right])`.
2. The question now is, if `height[left] < height[right]`, which side is limiting the area? The smallest height so if this is true `left` would be the limiting factor, also by checking the formula `area=width*min(height[left], height[right])` the smallest height either `left` or `right` will limit.
3. So the question is, can moving the `right` pointer increase the area?

I came from a big break again, but this is the solution:

```python
def solution_2(height: list[int]) -> int:
    left = 0
    right = len(height) - 1
    max_area = 0
    while left < right:
        local_area = min(height[left], height[right]) * (right - left)
        if local_area > max_area:
            max_area = local_area
        if height[left] > height[right]:
            right -= 1
        else:
            left += 1
    return max_area
```

Basically, we keep track of max area and iterate over all the array, important part here is whenever we decide to move a pointer we move the smaller value(the one limiting) in the hope of getting a better one.
