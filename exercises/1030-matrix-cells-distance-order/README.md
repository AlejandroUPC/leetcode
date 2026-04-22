#  Matrix Cells in Distance Order

## Problem


You are given four integers row, cols, rCenter, and cCenter. There is a rows x cols matrix and you are on the cell with the coordinates (rCenter, cCenter).

Return the coordinates of all cells in the matrix, sorted by their distance from (rCenter, cCenter) from the smallest distance to the largest distance. You may return the answer in any order that satisfies this condition.

The distance between two cells (r1, c1) and (r2, c2) is |r1 - r2| + |c1 - c2|.

 
*Example 1:*

Input: rows = 1, cols = 2, rCenter = 0, cCenter = 0

Output: [[0,0],[0,1]]

Explanation: The distances from (0, 0) to other cells are: [0,1]


*Example 2:*

Input: rows = 2, cols = 2, rCenter = 0, cCenter = 1

Output: [[0,1],[0,0],[1,1],[1,0]]

Explanation: The distances from (0, 1) to other cells are: [0,1,1,2]

The answer [[0,1],[1,1],[0,0],[1,0]] would also be accepted as correct.

*Example 3:*

Input: rows = 2, cols = 3, rCenter = 1, cCenter = 2

Output: [[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]]

Explanation: The distances from (1, 2) to other cells are: [0,1,1,2,2,3]

There are other answers that would also be accepted as correct, such as [[1,2],[1,1],[0,2],[1,0],[0,1],[0,0]].


## Approach

The examples in the are quite hard to visualize (at least to me), but instead of starting to think I will try to infer a solution first from the input/output of the example and work my way from there.

1. It's clear that one of the elements of the solution is always `(rCenter, cCenter)`.
2. The number of items in the array (whether a list or integer distance) is always `rows * cols`.
3. The values (when looking at the dist) seem to be an increasing serie.

Reached this point I'd need to try and do `rows = 2` and `cols = 3` maybe? But also what happens when we swap `rows` and `cols`? On the examples `rows>=cols` so not sure if we can make an assumption.

```markdown
rows = 1, cols = 2, rCenter = 0, cCenter = 0

 (0,0)
 (0,1)

solution = [(0, 0), (| 0 - 0|, | 0 - 1 |)] = [(0, 0), (0, 1)] = [0, 1]

rows = 2, cols = 2, rCenter = 0, cCenter = 1

 (0,0) (0,1)
 (1,0) (1,1)

solution = [(0, 1), (|0 - 0|, |0 - 1|), (|0 - 0| , |1 - 1|), (|0 - 1|, |1 - 1|)] = [(0, 1), (0, 0), (1, 1), (1, 0)] = [0, 1, 1, 2]

rows = 2, cols = 3, rCenter = 1, cCenter = 2

 (0,0) (0,1) (0,2)
 (1,0) (1,1) (1,2)

solution = [(|0 -0 |, |0 - 2|), (|0 - 0|, |1 - 2|), (|0 - 0|, |2 - 2|), (|0 - 1|, |0 -2 |), (|0 - 1|, |1 - 2|), (|0 - 1|, |2 - 2|)] = [(0,2), (0, 1), (0, 0), (1, 2), (1 ,1), (1, 0)] = [0, 1, 1, 2, 2, 3]

Now we do the case not reflected in example

rows = 2, cols = 3, rCenter = 1, cCenter = 3

 (0,0) (0,1) (0,2) (0,3)
 (1,0) (1,1) (1,2) (1,3)

solution? = [(|0 - 1|, |0 - 3|), (|0 - 1|, |1 - 3|), (|0 - 1|, |3 - 2|), (|0 - 1|, |3 - 3|), (|1 - 1|, |0 - 3|), (|1 - 1|, |1 - 3|), (|1 - 1|, |2 - 3|), (|1 - 1|, |2 - 3|), (|1 - 1|, |3 - 3|)] = [(1, 3), (1, 2), (1, 1), (1, 0), (0, 3), (0, 2), (0, 1), (0, 0)] = [4, 3, 2, 1, 3, 2, 1, 0] = [0, 1, 1, 2, 2, 3, 3, 4]

The last example we made up might be wrong?

```

After lookign at the examples, initially it does not seem to be an easy rule, also it depends a lot where the center is positioned so maybe there is no cool mathemetical trick but an efficient algorithm implementation, but the fact that the matrix is not given as input and just the params, we probaly can solve it without building a matrix like in the represntation above.

One of the first solutions, quite hardcoded that just computes distance but does not take into account order (we probably want to insert by order instead of sorting at the end):

```python
def solution(rows: int, cols: int, r_center: int, c_center: int) -> list[list[int]]:
    distances: list[list[int]] = []
    for r in range(rows):
        for c in range(cols):
            distance = (abs(r - r_center), abs(c - c_center))
            distances.append(list(distance))
    return distances
```

Probably can return a list sorted by the `lambda k: foo` where `foo` is just the abs between first cords such as:

```python
class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        distances: list[list[int]] = []
        for r in range(rows):
            for c in range(cols):
                distance = (abs(r - rCenter), abs(c - cCenter))
                distances.append(list(distance))
        return list(
            sorted(distances, key=lambda x: abs(x[0] - rCenter) + abs(x[1] - cCenter))
        )
```

This passed the test case but failed submission where input:
- rows = 3
- cols = 4
- rCenter = 0
- cCenter = 1

We outputed:

```markdown
[[0,1],[0,1],[0,0],[0,2],[1,1],[1,1],[1,0],[1,2],[2,1],[2,1],[2,0],[2,2]]
```

Expected:

```
[[0,1],[0,0],[0,2],[1,1],[0,3],[1,0],[1,2],[2,1],[1,3],[2,0],[2,2],[2,3]]
```

So we were clearly wrong, head to [learnings](#Learnings) I guess.

## Complexity

### Time: O(rows*cols)

We just ignore the sorting we do, othewrise would add but this would be a `O(rows*cols)` where the computation depends on those two parameters.


### Space: O(rows*cols)

Similar, each element we store in the distance list is 2 integers but the amount of istance we compute is directly corelated on how big the matrix is (rows and cols).

## Learnings

I effed up big time, I am actually computing distance twice, on append and on sorting, lol. Big missread on my end of the entire problem, should have not take a lunch break inbetween.

Here is the most similar solution that just builds the matrixs (literally what I complained about) and just computes the distance at the end by sorting:

```python
def solution(rows, cols, rCenter, cCenter):
    cells = []

    for r in range(rows):
        for c in range(cols):
            cells.append([r, c])

    return sorted(
        cells,
        key=lambda x: abs(x[0] - rCenter) + abs(x[1] - cCenter)
    )
```

This (now yes taking into account the sorting) is a `O(n log n)` issue, but there is a way to do it on `O(n)` using `BFS`.

The way to compute distance as:

`d = |r - rCenter| + |c - cCenter|` is known as Manhattan distance, and basically it tells let's you think in way of rings:

- Distance 0: You are the center
- Distance 1: First direct neighbors
- Distance 2: Next ring... and so on.

E.g if you had a diamond-shapped matrix:

```markdown
    *
  * * *
* * C * *
  * * *
    *
```

You can think as well as whenever in a 2d dimension space, each move up/down/left/right costs 1 (no diagonal); for example, for going from `(1, 1)` to `(3, 2)` you need:

- one up
- one up
- one right

`d = |3 - 1| + |2 - 1| = 3` as the 3 steps listed above.


### BFS

This is where `BFS` (Breadth-First Search), by its own nature, comes handy as it could be described an algorithm that explores everything that is closer, then goes further. You can think of the waves generated when you throw a stone in the water that keep expanding to further points (neighbords) but first does a small wave and it keeps expanding.

#### How it works

`BFS` can be based in a `FIFO` (First In First Out) queue where you put a starting point (`rCenter`, `cCenter`), on the first iteration you take it out and add its neighbors, and keep repeatin as it could be described an algorithm that explores everything that is closer, then goes further. You can think of the waves generated when you throw a stone in the water that keep expanding to further points (neighbords) but first does a small wave and it keeps expanding.

#### How it works

`BFS` can be based in a `FIFO` (First In First Out) queue where:

1. You put a starting point (`rCenter`, `cCenter`).
2. Take it out on the first iteration you take it out. 
3. Add its neighbors
4. Keep repeating.

So, what would the previous problem with a `BFS` approach look like?

```markdown
rows = 3, cols = 3, rCenter = 1, cCenter = 1.

(0,0) (0,1) (0,2)
(1,0) (1,1) (1,2)
(2,0) (2,1) (2,2)

And we need to return all the sorced ditance from (rCenter, cCenter) = (1, 1), distance described as |r - 1| + |c - 1|.

Step 0:

We start with our queue:

fifo_queue = [(1, 1)]
visisted = {(1, 1)}

So we are at:

.  .  .
. [C] .
.  .  .

So far result = [(1, 1)].

Step 1 - Explore Neighbors

From our prev visit (1, 1) we can now add (after removing (1, 1)):
fifo_queue = [(0, 1), (2, 1), (1, 0), (1, 2)], those are all dist = 1:

So we are at:

.  *  .
* [C] *
.  *  .

result = [(1, 1), 
            (0, 1), (2, 1), (1, 0), (1, 2)]

Step 2: Next ring(layer)

We now discover (what are the diagonal from center): `(0,0), (0,2), (2,0), (2,2)`, which are all distance 2:

*  *  *
* [C] *
*  *  *

result = [(1, 1),
            (0, 1), (2, 1), (1, 0), (1, 2),
            (0, 0), (0, 2), (2, 0), (2, 2)]

So `BFS` ensure that you will visit all neighbors of whatever graph, and you will see the neighbor `d` that is closer first before seeing the `d + 1`.
