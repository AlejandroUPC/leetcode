# Ransom Note

## Problem

Given two strings, `ransomNote` and `magazine`, make sure all the chards you need to write your `ransomNote` exist in `magazine`.

## Approach

First thought was a membership check but you also need to keep count, e.g if you want to write `Hello` but have `Helo` it will fail, given that to write a `ransomNote` that says `Hello` with membership (per single character) `Helo` would suffice but there are two `l`'s.

Second solution would be to build a counter on `magazine` and keep substracting on `ransomNote`, until we hit a 0 before substract.

## Complexity

### Time: O(n + m)

This is because in order to create the counter, we need to iterate through all the `magazine` to know how many characters and which are available, so we will iterate once, then again we need to iterate on `ransomNote` as we substract the counts of characters from `magazine`.

### Space: O(1)

We create a new counter which should be unique characters (<= 26), so it should be `O(k)` but as its bounded we can assume constant `O(1)`.


## Learnings

There are even two more elegants ways to solve this, one is to directly substract counters, so `not (Counter(ransomNote) - Counter(magazine))`, making sure if you take away all the characters from `ransomNote` using `magazine` you get an empty set, then negated = True. This is because Counter just will ignore negatives (e.g if you have more in magazine).

The second one, and more DSA-based is using ordinals, which is quite cool.

### Small ordinals intro

Ordinals are nothing but a way to convert strings to numbers, as computers work with numbers (ASCII/Unicode), in a way that :

```markdown
a = 97
b = 98
...
z = 122
```

There is some cool stuff about this we saw already in CS50 (uppercases are modular, I think). Using arrays and accesing by index is faster than hashing, and we trust that every position in the array will be alphabetically, in order to achieve so, we check the  value of the first letter `a`:

```python
>>> ord('a')
97
```

So to reset and make sure all the letters start at 0 and continuously, we first create an empty array of 26 positions and keep adding:

```python
count = [0] * 26

for letter in 'abcda':
    count[ord(letter) - ord('a')] += 1
print(count)

[2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```

So we obtain in index 0 there are two letters, so two characters in `a` in the string we passed.

The entire problem then could look something as the `solution_2` implemented, not necessarely hard to see the difference on accessing by the actual character vs its ordinal, both solution are omptimal in terms of time `O(m+n)` as we iterate both arrays twice, and of space as we create a constant amount of variables (we could discuss that the counter will grow as magazine, while the array for character is contained at  26 when we create it `[0] * 26` , but we assume the counter as well so really it'd be `O(k)` but is bounded `<=26 -> O(1)`.

One can also say though, and according to a correction that the space complexity it's really constrained by the amount of characters repeated in magazine, as we store the integers and they become bigger to `O(logn)`.
