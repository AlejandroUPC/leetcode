# Count Distinct Numbers on Board

You are given a positive integer n, that is initially placed on a board. Every day, for 109 days, you perform the following procedure:

- For each number x present on the board, find all numbers 1 <= i <= n such that x % i == 1.
- Then, place those numbers on the board.
- Return the number of distinct integers present on the board after 109 days have elapsed.

Note:

- Once a number is placed on the board, it will remain on it until the end.
- % stands for the modulo operation. For example, 14 % 3 is 2.
 

Example 1:

Input: n = 5

Output: 4

Explanation: Initially, 5 is present on the board. 

The next day, 2 and 4 will be added since 5 % 2 == 1 and 5 % 4 == 1. 

After that day, 3 will be added to the board because 4 % 3 == 1. 

At the end of a billion days, the distinct numbers on the board will be 2, 3, 4, and 5. 

Example 2:

Input: n = 3

Output: 2

Explanation: 

Since 3 % 2 == 1, 2 will be added to the board. 

After a billion days, the only two distinct numbers on the board are 2 and 3. 
 

## Problem

There seems to be a lot of stuff, a bit hard to untangle the actual question and could be better written but seems to be a kind of recursive function.


## Approach

It also runs for a lot of loops (10^9) so I'm sure there is a way to improve this (recursion+cache on params?, kinda like fibonacci?), my first approach is probably wrong and might not even do what the problems wants (not I did the inputs to avoid getting flooded with logs):

```python
def solution(n: int) -> int:
    board: list[int] = [n]
    for day in range(0, (10**9) + 1):
        to_add = []
        input(f"Working on {day=}.")
        for number in board:
            input(f"Working on {number=} of {board=}.")
            for num_check in range(1, n + 1):
                input(f"Checking {num_check=} vs {number=}.")
                if number % num_check == 1:
                    print(f"Bing on {number}%{num_check}={number % num_check}.")
                    if num_check not in board:
                        to_add.append(num_check)
        board.extend(to_add)
        input(f"After {day=} we got {board=}.")
    return len(board)
```

This produced the following output for day 1, 2 and 3 that matches the example 1:

```markdown
Working on day=1.
Working on number=5 of board=[5].
Checking num_check=1 vs number=5.
Checking num_check=2 vs number=5.
Bing on 5%2=1.
Checking num_check=3 vs number=5.
Checking num_check=4 vs number=5.
Bing on 5%4=1.
Checking num_check=5 vs number=5.
**After day=1 we got board=[5, 2, 4].**
Working on day=2.
Working on number=5 of board=[5, 2, 4].
Checking num_check=1 vs number=5.
Checking num_check=2 vs number=5.
Bing on 5%2=1.
Checking num_check=3 vs number=5.
Checking num_check=4 vs number=5.
Bing on 5%4=1.
Checking num_check=5 vs number=5.
Working on number=2 of board=[5, 2, 4].
Checking num_check=1 vs number=2.
Checking num_check=2 vs number=2.
Checking num_check=3 vs number=2.
Checking num_check=4 vs number=2.
Checking num_check=5 vs number=2.
Working on number=4 of board=[5, 2, 4].
Checking num_check=1 vs number=4.
Checking num_check=2 vs number=4.
Checking num_check=3 vs number=4.
Bing on 4%3=1.
Checking num_check=4 vs number=4.
Checking num_check=5 vs number=4.
**After day=2 we got board=[5, 2, 4, 3].**
```

At this point there are two things crossing my mind:

1. Let's just run it til the end.
2. Based on the logs, and the never ending increased board size, a lot of ops might be repeated.


Like the final solution aftery day 2 already contains the final solution `[2, 3, 4, 5]` that returns 4, so there must be indeed a much easier way to compute this, baseed on logs:

```markdown
After day=13458806 we got board=[5, 2, 4, 3].
Working on day=13458807.
Working on number=5 of board=[5, 2, 4, 3].
Checking num_check=1 vs number=5.
Checking num_check=2 vs number=5.
Bing on 5%2=1.
Checking num_check=3 vs number=5.
Checking num_check=4 vs number=5.
Bing on 5%4=1.
Checking num_check=5 vs number=5.
Working on number=2 of board=[5, 2, 4, 3].
Checking num_check=1 vs number=2.
Checking num_check=2 vs number=2.
Checking num_check=3 vs number=2.
Checking num_check=4 vs number=2.
Checking num_check=5 vs number=2.
Working on number=4 of board=[5, 2, 4, 3].
Checking num_check=1 vs number=4.
Checking num_check=2 vs number=4.
Checking num_check=3 vs number=4.
Bing on 4%3=1.
Checking num_check=4 vs number=4.
Checking num_check=5 vs number=4.
Working on number=3 of board=[5, 2, 4, 3].
Checking num_check=1 vs number=3.
Checking num_check=2 vs number=3.
Bing on 3%2=1.
Checking num_check=3 vs number=3.
Checking num_check=4 vs number=3.
Checking num_check=5 vs number=3.
After day=13458807 we got board=[5, 2, 4, 3].
Working on day=13458808.
Working on number=5 of board=[5, 2, 4, 3].
Checking num_check=1 vs number=5.
Checking num_check=2 vs number=5.
Bing on 5%2=1.
Checking num_check=3 vs number=5.
Checking num_check=4 vs number=5.
Bing on 5%4=1.
Checking num_check=5 vs number=5.
Working on number=2 of board=[5, 2, 4, 3].
Checking num_check=1 vs number=2.
Checking num_check=2 vs number=2.
Checking num_check=3 vs number=2.
Checking num_check=4 vs number=2.
Checking num_check=5 vs number=2.
Working on number=4 of board=[5, 2, 4, 3].
Checking num_check=1 vs number=4.
Checking num_check=2 vs number=4.
Checking num_check=3 vs number=4.
Bing on 4%3=1.
Checking num_check=4 vs number=4.
Checking num_check=5 vs number=4.
Working on number=3 of board=[5, 2, 4, 3].
Checking num_check=1 vs number=3.
Checking num_check=2 vs number=3.
Bing on 3%2=1.
Checking num_check=3 vs number=3.
Checking num_check=4 vs number=3.
Checking num_check=5 vs number=3.
After day=13458808 we got board=[5, 2, 4, 3].
Working on day=13458809.
Working on number=5 of board=[5, 2, 4, 3].
Checking num_check=1 vs number=5.
Checking num_check=2 vs number=5.
Bing on 5%2=1.
Checking num_check=3 vs number=5.
Checking num_check=4 vs number=5.
Bing on 5%4=1.
Checking num_check=5 vs number=5.
Working on number=2 of board=[5, 2, 4, 3].
Checking num_check=1 vs number=2.
Checking num_check=2 vs number=2.
Checking num_check=3 vs number=2.
Checking num_check=4 vs number=2.
Checking num_check=5 vs number=2.
Working on number=4 of board=[5, 2, 4, 3].
Checking num_check=1 vs number=4.
Checking num_check=2 vs number=4.
Checking num_check=3 vs number=4.
Bing on 4%3=1.
Checking num_check=4 vs number=4.
Checking num_check=5 vs number=4.
Working on number=3 of board=[5, 2, 4, 3].
Checking num_check=1 vs number=3.
Checking num_check=2 vs number=3.
Bing on 3%2=1.
Checking num_check=3 vs number=3.
Checking num_check=4 vs number=3.
Checking num_check=5 vs number=3.
After day=13458809 we got board=[5, 2, 4, 3].
Working on day=13458810.
Working on number=5 of board=[5, 2, 4, 3].
Checking num_check=1 vs number=5.
Checking num_check=2 vs number=5.
Bing on 5%2=1.
Checking num_check=3 vs number=5.
Checking num_check=4 vs number=5.
Bing on 5%4=1.
Checking num_check=5 vs number=5.
Working on number=2 of board=[5, 2, 4, 3].
Checking num_check=1 vs number=2.
Checking num_check=2 vs number=2.
Checking num_check=3 vs number=2.
Checking num_check=4 vs number=2.
Checking num_check=5 vs number=2.
Working on number=4 of board=[5, 2, 4, 3].
Checking num_check=1 vs number=4.
Checking num_check=2 vs number=4.
Checking num_check=3 vs number=4.
Bing on 4%3=1.
Checking num_check=4 vs number=4.
Checking num_check=5 vs number=4.
Working on number=3 of board=[5, 2, 4, 3].
Checking num_check=1 vs number=3.
Checking num_check=2 vs number=3.
Bing on 3%2=1.
Checking num_check=3 vs number=3.
Checking num_check=4 vs number=3.
Checking num_check=5 vs number=3.
After day=13458810 we got board=[5, 2, 4, 3].
Working on day=13458811.
Working on number=5 of board=[5, 2, 4, 3].
Checking num_check=1 vs number=5.
Checking num_check=2 vs number=5.
Bing on 5%2=1.
Checking num_check=3 vs number=5.
Checking num_check=4 vs number=5.
Bing on 5%4=1.
Checking num_check=5 vs number=5.
Working on number=2 of board=[5, 2, 4, 3].
Checking num_check=1 vs number=2.
Checking num_check=2 vs number=2.
Checking num_check=3 vs number=2.
Checking num_check=4 vs number=2.
Checking num_check=5 vs number=2.
Working on number=4 of board=[5, 2, 4, 3].
Checking num_check=1 vs number=4.
Checking num_check=2 vs number=4.
Checking num_check=3 vs number=4.
Bing on 4%3=1.
Checking num_check=4 vs number=4.
Checking num_check=5 vs number=4.
Working on number=3 of board=[5, 2, 4, 3].
Checking num_check=1 vs number=3.
Checking num_check=2 vs number=3.
Bing on 3%2=1.
Checking num_check=3 vs number=3.
Checking num_check=4 vs number=3.
Checking num_check=5 vs number=3.
After day=13458811 we got board=[5, 2, 4, 3].
Working on day=13458812.
Working on number=5 of board=[5, 2, 4, 3].
Checking num_check=1 vs number=5.
Checking num_check=2 vs number=5.
Bing on 5%2=1.
Checking num_check=3 vs number=5.
Checking num_check=4 vs number=5.
Bing on 5%4=1.
Checking num_check=5 vs number=5.
Working on number=2 of board=[5, 2, 4, 3].
Checking num_check=1 vs number=2.
Checking num_check=2 vs number=2.
Checking num_check=3 vs number=2.
Checking num_check=4 vs number=2.
Checking num_check=5 vs number=2.
Working on number=4 of board=[5, 2, 4, 3].
Checking num_check=1 vs number=4.
Checking num_check=2 vs number=4.
Checking num_check=3 vs number=4.
Bing on 4%3=1.
Checking num_check=4 vs number=4.
Checking num_check=5 vs number=4.
Working on number=3 of board=[5, 2, 4, 3].
Checking num_check=1 vs number=3.
Checking num_check=2 vs number=3.
Bing on 3%2=1.
Checking num_check=3 vs number=3.
Checking num_check=4 vs number=3.
Checking num_check=5 vs number=3.
After day=13458812 we got board=[5, 2, 4, 3].
Working on day=13458813.
Working on number=5 of board=[5, 2, 4, 3].
Checking num_check=1 vs number=5.
Checking num_check=2 vs number=5.
Bing on 5%2=1.
Checking num_check=3 vs number=5.
Checking num_check=4 vs number=5.
Bing on 5%4=1.
Checking num_check=5 vs number=5.
Working on number=2 of board=[5, 2, 4, 3].
Checking num_check=1 vs number=2.
Checking num_check=2 vs number=2.
Checking num_check=3 vs number=2.
Checking num_check=4 vs number=2.
Checking num_check=5 vs number=2.
Working on number=4 of board=[5, 2, 4, 3].
Checking num_check=1 vs number=4.
Checking num_check=2 vs number=4.
Checking num_check=3 vs number=4.
Bing on 4%3=1.
Checking num_check=4 vs number=4.
Checking num_check=5 vs number=4.
Working on number=3 of board=[5, 2, 4, 3].
Checking num_check=1 vs number=3.
Checking num_check=2 vs number=3.
Bing on 3%2=1.
Checking num_check=3 vs number=3.
Checking num_check=4 vs number=3.
Checking num_check=5 vs number=3.
After day=13458813 we got board=[5, 2, 4, 3].
```


Here is after adding some ugly memoization, runs in 30 secs for n = 5:

```python3
def solution(n: int) -> int:
    board: list[int] = [n]
    memo: set = set()  # this is to not re-compute board, if we computed board once it will be same results
    for day in range(1, (10**9) + 1):
        if tuple(board) in memo:
            # print("Continue")
            continue
        memo.add(tuple(board))
        to_add = []
        print(f"Working on {day=}.")
        for number in board:
            print(f"Working on {number=} of {board=}.")
            for num_check in range(1, n + 1):
                print(f"Checking {num_check=} vs {number=}.")
                if number % num_check == 1:
                    print(f"Bing on {number}%{num_check}={number % num_check}.")
                    if num_check not in board:
                        to_add.append(num_check)
        board.extend(to_add)
        print(f"After {day=} we got {board=}.")
    return len(board)
```

It generates the following logs, see that after day `3`, out of `10**9`:

```markdown
Working on day=1.
Working on number=5 of board=[5].
Checking num_check=1 vs number=5.
Checking num_check=2 vs number=5.
Bing on 5%2=1.
Checking num_check=3 vs number=5.
Checking num_check=4 vs number=5.
Bing on 5%4=1.
Checking num_check=5 vs number=5.
After day=1 we got board=[5, 2, 4].
Working on day=2.
Working on number=5 of board=[5, 2, 4].
Checking num_check=1 vs number=5.
Checking num_check=2 vs number=5.
Bing on 5%2=1.
Checking num_check=3 vs number=5.
Checking num_check=4 vs number=5.
Bing on 5%4=1.
Checking num_check=5 vs number=5.
Working on number=2 of board=[5, 2, 4].
Checking num_check=1 vs number=2.
Checking num_check=2 vs number=2.
Checking num_check=3 vs number=2.
Checking num_check=4 vs number=2.
Checking num_check=5 vs number=2.
Working on number=4 of board=[5, 2, 4].
Checking num_check=1 vs number=4.
Checking num_check=2 vs number=4.
Checking num_check=3 vs number=4.
Bing on 4%3=1.
Checking num_check=4 vs number=4.
Checking num_check=5 vs number=4.
After day=2 we got board=[5, 2, 4, 3].
Working on day=3.
Working on number=5 of board=[5, 2, 4, 3].
Checking num_check=1 vs number=5.
Checking num_check=2 vs number=5.
Bing on 5%2=1.
Checking num_check=3 vs number=5.
Checking num_check=4 vs number=5.
Bing on 5%4=1.
Checking num_check=5 vs number=5.
Working on number=2 of board=[5, 2, 4, 3].
Checking num_check=1 vs number=2.
Checking num_check=2 vs number=2.
Checking num_check=3 vs number=2.
Checking num_check=4 vs number=2.
Checking num_check=5 vs number=2.
Working on number=4 of board=[5, 2, 4, 3].
Checking num_check=1 vs number=4.
Checking num_check=2 vs number=4.
Checking num_check=3 vs number=4.
Bing on 4%3=1.
Checking num_check=4 vs number=4.
Checking num_check=5 vs number=4.
Working on number=3 of board=[5, 2, 4, 3].
Checking num_check=1 vs number=3.
Checking num_check=2 vs number=3.
Bing on 3%2=1.
Checking num_check=3 vs number=3.
Checking num_check=4 vs number=3.
Checking num_check=5 vs number=3.
After day=3 we got board=[5, 2, 4, 3].
4
uv run python 2549-count-distinct-numbers-board/main.py  34.21s user 0.05s system 99% cpu 34.280 total
```

Similar to `n=3`:

```markdown
Working on day=1.
Working on number=3 of board=[3].
Checking num_check=1 vs number=3.
Checking num_check=2 vs number=3.
Bing on 3%2=1.
Checking num_check=3 vs number=3.
After day=1 we got board=[3, 2].
Working on day=2.
Working on number=3 of board=[3, 2].
Checking num_check=1 vs number=3.
Checking num_check=2 vs number=3.
Bing on 3%2=1.
Checking num_check=3 vs number=3.
Working on number=2 of board=[3, 2].
Checking num_check=1 vs number=2.
Checking num_check=2 vs number=2.
Checking num_check=3 vs number=2.
After day=2 we got board=[3, 2].
2
uv run python 2549-count-distinct-numbers-board/main.py  29.39s user 0.06s system 99% cpu 29.467 total
```

We reached the final result on day `2` and then do a lot of unncessary for loops that at least are memoized on `board`, so we save some time.

So it looks like the result, based on those two cases is always `n - 1`.


## Complexity

Note that this solution times out on leetcode so probably its very wrong.

### Time: O(n^3)

Its `O(num_days x board_size x n) = O(n^3)`, but in order to memo we creata a look up that would add some over head.

### Space: O(n^2)

So there is the board, `O(n)` and then we also create a memo to keep many states, so it could be as much as `O(n^2)`.

## Learnings


Here we are going to dig deep in the math foundation that makes this problem much easier after investigating and looking at other solutions.

What seems to be the case is that, at one point of the `10**9` fix iterations (we repeat for a fixed amount of days) the solution converges, and we keep iterating over the same board over and over.

There is also a fix part in this problem is that the numbers we check in the denominator for each number on the board, which seems to be `range(1,n+1)`, given that `n` does not change and.

The condition to add (mutate) any item on the board is that a number `x % y == 1`, where `x` is the current number in the board, and `y` is a number we are checking if we can add from `1` to `n`.

A written example of the iterations for `n = 5` might be useful:

```markdown
Starting:

n = 5
board = {5}
numbers to test (1, 2, 3, 4, 5):

So for each number `x` on the board we check all individually `y` for number to test:
5 % 1 == 0
5 % 2 == 1
5 % 3 == 2
5 % 4 == 1
5 % 5 == 0

Only 2 and 4 are passing and being added to the board, so we have now:

n = 5
board = {5, 4, 2}
numbers to test (1, 2, 3, 4, 5)

We repeat the check for 4 in this case (we did 5 already):
4 % 1 == 0
4 % 2 == 0
4 % 3 == 1
4 % 4 == 0

And 2:

2 % 1 == 0
2 % 2 == 0

We add just 3

n = 5
board = {5, 4, 2, 3}
numbers to test (1, 2, 3, 4, 5)

We check just 3 as the others we tested already:

3 % 1 == 0
3 % 2 == 1
3 % 3 == 0

We could add 2 already but is present.

At this point we are not adding any new number to the set so we will just repeat (maybe this would be a way to shortcircuit? and end earlier).
```

Now let's look when we got `1` as a resulting of the modulo:

- 5 -> {4, 2}
- 4 -> {3}
- 3 -> {2}
- 2 -> {}

So it looks, that the same solution can be written (taken into consideration we take unique values) as:

- 5 -> {4} # 2 is obtained from three later on
- 4 -> {3}
- 3 -> {2}

So for any given number, we can be sure that we can obtain a number `x -> x - 1` from `n` to `0`, or another perspective for any `n` the solution is `{2, ..., n}`, and this is true because `x % (x - 1) = 1` (kinda makes sense as any number substracting one, the residuo from modulo will be 1 for positive).

This seems to converge as:

`n -> n - 1 -> n - 2 -> ... -> 2` as any number substract until you reach 2, for 5:

- 5     = 5
- 5 - 1 = 4
- 5 - 2 = 3
- 5 - 3 = 2

So, to sum it up, we can assume that for any `n` we can generate all numbers down to 2 (% 1 == 0, we can't generate 1), so the solution will be `n - 1`, that easy, that simple.

```python3
def solution(n: int) -> int:
    if n == 1:
        return n
    return n - 1
```

Nice learning, got humbled

