# Number of steps to Reduce a Number to Zero 

## Problem

Given an integer num, return the number of steps to reduce it to zero.

In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

The number is between 0 and 10^6. 

Example 1:

Input: num = 14
Output: 6
Explanation: 
Step 1) 14 is even; divide by 2 and obtain 7. 
Step 2) 7 is odd; subtract 1 and obtain 6.
Step 3) 6 is even; divide by 2 and obtain 3. 
Step 4) 3 is odd; subtract 1 and obtain 2. 
Step 5) 2 is even; divide by 2 and obtain 1. 
Step 6) 1 is odd; subtract 1 and obtain 0.
Example 2:

Input: num = 8
Output: 4
Explanation: 
Step 1) 8 is even; divide by 2 and obtain 4. 
Step 2) 4 is even; divide by 2 and obtain 2. 
Step 3) 2 is even; divide by 2 and obtain 1. 
Step 4) 1 is odd; subtract 1 and obtain 0.
Example 3:

Input: num = 123
Output: 12

## Approach

Kind of recursive approach (or while {condition}) where we just keep whilin' until we meet condition, base cases are either divice between 2 and or -1 on num.

## Complexity

100% beats mem (huh, error I think) on LC suite.

### Time: O(log(n))

As explained in [learnings](##Learnings), when thinking of integers we need to compute our size as number of bits, and we are basically doing two operations:

1. Dividing
2. Substracting

We can assume that dividing will happen most often than substracting (e.g dividing by 2 and obtaining another number divisible by 2), and we will not be stopping until we reach < 1 (approx 1).

So for the division operations, we can express them as `n/(2^k)`, e.g imagine we don't ever need to substract:

```markdown
1 -> 16 / 2 = 8
2 -> 8 / 2 = 4
3 -> 4 / 2 = 2
4 -> 2 / 2 = 1
5 -> 1 / 2 = 0.5 (0) # we omit these and stop at 1 though
```

We could express as

```markdown
16/2^4 ~= 1
```

If we go fromn `n/(2^k) ~= 1` then `n = 2^k` so `k = log_2(n)`, the division and number of steps happens like `log(n)` times.

Worst case scenario for substraction is to have one substraction per each division (e.g n=7) so we could say `2 log (n)` but on `O` we jus remoe constants, so its `O(log(n))`.



### Space: O(1)

We do not really allocate more memory as `n` grows, and `cter` is just a modification of a number step by step.



## Learnings

In these kinds of problems, when input is not an array we think (and usually work) as `n` as bits, so basically the size of an integer `n` becomes `log_2(n)`, we are looking
at then an input that grows from size `log_2(0)` up until `log_2(1000000)` which is `0 <= n <= 20`.

### Bits basics

Different way of thinking of numbers in binary base, it's just a 1 or a 0.

The number of bits of a number `n` can be expressed as:

```plaintext
bits(n) = log_2(n) + 1
```

When concatenating some numbers its just the 2^{position} sum:

```plaintext
Binay 1101
     1   1   0   1 
13 = 8 + 4 + 0 + 1
   = 2^3 + 2^2 + 2^0
```

##### Core

Very basic operations:

**AND (&)**

Defined as `(a&b)_i = a_i * b_i`, means that bit is only 1 if both are 1.

```plaintext
a = 1101 (13)
b = 1011 (11)

a & b = 1001 (9)
```

How is this working? Really if we can write any integer in base 2 as `n = 2q + r, r{0,1}`, so we can then  have a small table:

```markdown
| q | r | n |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 8 | 0 | 16|
| 8 | 1 | 17|
```

It seems that the value of `r` might indicate whether if a number is odd or even, given that for any integer `n`, `2^n` will be always pair, and the last number `r` will be in charge of deciding whether if this number is odd or even.

Note: this last bit is called the least significant bit(LSB).

So let's take the previous examples for `16` and `17` and apply the `& 1`:

```markdown
16 = 10000 = 1 * 2^4 + 0 * 2^3 + 0 * 2^2 + 0 * 2^1 + 0 * 2^0 = sum([value_bit  * 2^{pos_bit}) # also note the LSB is 0!
17 = 10001 = 1 * 2^4 + 0 * 2^3 + 0 * 2^2 + 0 * 2^1 + 1 * 2^0 = sum([value_bit  * 2^{pos_bit}) # also note the LSB is 1!
```

We apply the `& 1` mask (vertical repr):

```markdown
10000
00001
-----
00000

16 & 1 = 0

10001
00001
-----
00001

17 & 1 = 1

```

So it looks like just by doing `& 1` and checking the outcome, 0 or 1, the number will be even or odd.

In problems usually this can be used to keep only specific bits (masking, like we are doing to check odd or even we keep last) or remove loest 1 `n & (n - 1)`.



** OR (|)**

Can be defined as `(a|b)_i = max(a_i,b_i)`, for example:

```markdown
1100
1010
----
1110
```

Also thought as, turn ON bits if any is ON, so it builds a new number by making the union of both active bits, but **never turns them off**.
It has the following properties:

1. Identity `(a|0) = a` because `max(a_i, 0) = a_i`.
2. Idempotent `a|a=a`.
3. Commutative `a|b=b|a`.
4. Associative `(a|b)|c = a|(b|c)`.
5. Important inequality: `a|b>=max(a,b)` as it can only turn bits on, never off, so it will always be the same or bigger.

Usually the most basic operation is the "ability" to turn certain bits ON, e.g:


```markdown
1 << 0 = 0001 = 1
1 << 1 = 0010 = 2
1 << 2 = 0100 = 4
1 << 3 = 1000 = 8
```
The above basically means do an or in the `nth` position, and we can assure that this bit (regardless of prev state, ON or OFF) will be ON.

This can be expressed as, for a bit `n` then we say to turn the bit on the position `i` as `n | (1 << i)`, se the following example:

```makrdown
n = 9 = 1001
i = 1

n | (1 << 1)

1001
0010
----
1011 = 11
```

Note that we have been using just one bit swaps right no, but we can create masks with more than one `1` to alter enable bits by creating masks such as:

```markdown
mask = (1 << 3) - 1 # 1 << 3 is 1000 = 8 - 1 = 7
mask = 7 = 0111 # so now we have a 3 bit mask!
n = 1000

n | mask = n | ((1 << 3) - 1)

1000
0111
----
1111 = 15
```

So basically there are two things here to keep in mind:

1. Turn ON the `nth` position bit as `n | (1 << i)`.
2. Turn ON the last `kth` bits as `n | ((1 << i) - 1)`.


** XOR (^) **

This operationw hat it does is when applied between two bits is set them ON if the states do not match, truth table:

```markdown
| a | b | R |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |
```
A more complex example:

```markdown
n = 13
m = 11 
n ^ m

1101
1011
----
0110 = 6
```

It can be expressed as `(a ^ b)_i = (a_i+b_i)mod2`.

We can say that XOR behaves like an adition without carry or mod2 addition, see the followign (lengthy example):

```markdown

If we have 1 in binary and add it twice:

 1
+1
---
10 (2 in decimal)

So what happened? we took down the 0 (first col) and carried 1 to the next, so XOR is like just carrying as:

1 ^ 1 = 0 or (1+1)mod2 = 0.

A more complex example, a normal sum:

 1101 (13)
+1011 (11)
-----
11000 (24)

If we XOR this in the bit world

 1101 (13)
^1011 (11)
-----
0110 = 6
```

An "easy" way to visualize this could be as:

```markdown
13 = 1101 = 8 + 4 + 0 + 1
11 = 1011 = 8 + 0 + 2 + 1

What do those not share? 4 and 2 = 6
```

This is useful in DSA sometimes because it is like doing an additionm but ignoring any overflow, e'g duplicates cancel out:

1. `x ^ x = 0` as all are equals.
2. It's reversible `a ^ b ^ b = a`.

### Reimplemntation using bits.

Just the odd/even part, not bothered with bit substraction yet:

```python3
def solution(num: int) -> int:
    cter = 0
    while num > 0:
        if not bool(int(num) & 1):
            num >>= 1
        else:
            num -= 1
        cter += 1
        print(num, cter)
    return cter


if __name__ == "__main__":
    print(solution(num=14))
```
