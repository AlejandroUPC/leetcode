# Matrix Diagonal Sum

## Problem

Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal. 

Example 1:

Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]

Output: 25

Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25

Notice that element mat[1][1] = 5 is counted only once.


Example 2:

Input: mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]

Output: 8

Example 3:


Input: mat = [[5]]

Output: 5

Using nested arrays its a common way to represent matrix in code, we probably need a sort of array where when we meet a diagonal (row==+-col, then we are in the diagonal) and store somehow those numbers.

## Approach

The first solution will be to have a two nested loops and keep count on which list we are (row) and which item in the list we are (col) and find out if we are diagonal, for both directions.

Actually, the diagonal, (left->right first) can be computed as every col, starting to 0 we read each position +1 until we reach the end, given that the matrix is square (`nxn`), we can assume length of the first arrays will be the length of all the nested arrays.

So this seems to be a case of two points for each array, when one starts on the left, one on the right and we keep decreasing, so basically for the matrix:

```markdown
[ 1   2   3 ]
[ 4   5   6 ]
[ 7   8   9 ]
```
We go like, step by step:

```markdown

step 1

Row index = 0

[ 1   2   3 ]
  ↑       ↑
 LR=0    RL=2

step 2

Row index = 1

[ 4   5   6 ]
    ↑
  LR=1
    ↑
  RL=1

Row index = 2

[ 7   8   9 ]
  ↑       ↑
 LR=2    RL=0

```

Note that for matrix where `n` is odd, we will have a common moment where the same row will be pointing at the same index, we need to take this into account, so we just sum the number once (`5` in this case on step 2).


## Complexity


### Time: O(n)

For the time complexity we are just iterating once per row, so it will be a single for loop depending on how big the matrix is `O(n)`.

### Space: O(n)

For the space complexity we are really just creating two pointers and a new variable, but those are constant so `O(1)`.

## Learnings

Not a lot to learn here other than a more elegant solution, were indeed we can base all of our positions (instead of declaring two pointers) based on range, if we think of our previous matrix as `(x, y)` coords:

```markdown
(0,0) (0,1) (0,2)
(1,0) (1,1) (1,2)
(2,0) (2,1) (2,2)
```

Here what we need to sum is:

1. primary diagonal (left-right): (0,0), (1,1), (2,2)
2. secondary diagonal (right-left) = (0,2), (2,0) # not we delegate the (1,1) to the primary

If we then iterate over `range(n)`, which produces (0, 1, 2), we can build both diagonals as :

1. primary diagonal `(i, i) = (0,0), (1, 1), (2, 2)`
2. secondary diagonal as `(i, n - 1 - i) = (0, 3 - 1 -0), (2, 3 - 1 -2) = (0, 2), (2, 0)` if we alsoo make sure that we don't compute if `i != n - 1 -i`, which is the center as `(1, 3 - 1  - 1) = (1, 1)`.


So one of the takeaways is that the secondary diagonal is nothing but the mirrored primary diagonal.
