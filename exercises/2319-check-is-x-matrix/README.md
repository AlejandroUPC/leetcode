# Check if Matrix Is X-Matrix

## Problem

A square matrix is said to be an X-Matrix if both of the following conditions hold:

1. All the elements in the diagonals of the matrix are non-zero.
2. All other elements are 0.

Given a 2D integer array grid of size n x n representing a square matrix, return true if grid is an X-Matrix. Otherwise, return false.

Example 1:

Input: grid = [[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]

Output: true

Explanation: Refer to the diagram above. 

An X-Matrix should have the green elements (diagonals) be non-zero and the red elements be 0.

Thus, grid is an X-Matrix.


Example 2:

Input: grid = [[5,7,0],[0,3,1],[0,5,0]]

Output: false

Explanation: Refer to the diagram above.

An X-Matrix should have the green elements (diagonals) be non-zero and the red elements be 0.

Thus, grid is not an X-Matrix.


## Approach

Seems a similar approach to the diagonal sum, where instead this case all-non diagonal elements should be == 0? We will need to iterate,
additionally, although this is the very ugly solution I came up with, the formula could be something like:

1. For first and last row all but idx 0 and len(matrix)- 1 should sum = 0 
2. for the rest only first and last should sum 0.

The following viz might help: #TODO: add viz


Tried for a while with this (ugly) solution which passed the run on LC but not the submissions for a huge matrix:

```python
class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        for i, row in enumerate(grid):
            if i == 0 or i == len(grid) - 1:
                if not sum(row[1 : len(grid) - 1]) == 0 or row[0] == 0 or row[-1] == 0:
                    return False
            else:
                if not sum([row[0], row[-1]]) == 0 or 0 in [row[1 : len(grid) - 1]]:
                    return False
        return True
```

This was def a messy solution that I ended up discarding and needed additional solutions. We already knew how to to check the diagonals of a matrix sum with a single loop, and it's true we can just compute diagonals of a matrix with a single pass:

```markdown
when iterating with `i` there are two diagonals, one left to right (primary) which is basically always (i, i), now the other secondary diagonal (right to left) is slightly trickier as we need to invert the order.

The secondary diagonal then, must:
1. Share the same `i`, as we do one pass per row.
2. Move in the "contrary" direction of `i`, from right to left.
3. Start from the the end (if its a 3x3 matrix, it will need to start from idx 2 (start from 0, so 0,1,2=3)).

So this can be writen as (i, n - 1 - i). Again very clear, the first element of the tuple is simple, same row. The `n - 1` means we are starting the array from behind and the `- i` is that on each iteration we move one place.

Having the following matrix we then:

[ 1  2  3 ]
[ 4  5  6 ]
[ 7  8  9 ]

Write as a cords tuple:

(0,0) (0,1) (0,2)
(1,0) (1,1) (1,2)
(2,0) (2,1) (2,2)

Now we start our looping for `n = 3`:

### Step 1 (i = 0):

first diagonal will be `(i, i) = (0, 0) = 1`.
second diagonal will be `(i, n - 1 - i) = (0, 3 - 1 - 0) = (0, 2) = 3`.

### Step 2 (i = 1)

first diagonal is `(i, i) = (1 ,1) = 5`.
second diagonal will be `(i, n - 1 - i) = (1, 3 - 1 - 1) = (1, 1) = 5`.
Here we are at the "common mid".

### Step 3 (i = 2) and last

first diagonal is `(i, i) = (3, 3) = 9`.
second diagonal is `(i, n - 1 - i) = (2, 0) = 7`.

```

It's also important that for `n = odd` matrix dimensions we will walk through the mide twice in some cases, we can avoid this by checking that both coords `i` and `n - 1 - i` are the same we just sum one, so we cave to have a check when we are chec


## Complexity

### Time: O(n^2)

We iterate just once for every row and then once again per row in a nested manner so `O(n) * O(n) = O(n^2)`.

### Space: O(1)

We create no additional variables, should be `O(1)`.

## Learnings


Left most of the learnings above, but basically my first approach where checking fist and last row (as they behave differently) was not enough, most of matrix problems based (unless just diagonal), are `(i, j)` based and requeire `O(n^2)`, instead of thinking of rows we have to think of cells.
