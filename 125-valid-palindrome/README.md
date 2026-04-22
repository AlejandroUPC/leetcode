# Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 
## Example 1:

```markdown
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
```

## Example 2:

```markdown
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
```

## Example 3:


```markdown
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
```

## Problem

Response seems quite easy, it can probably be by just reverting the (lower casing) and a bit of a one line, not sure of the complexity though.

## Approach

So we can easily reverse a string (and filter the chars we want) and cast to lower and it should be the same if its a palindrome:

```python
def solution(s: str) -> bool:
    return "".join(c for c in s[::-1].lower() if c.isalnum()) == "".join(
        c for c in s.lower() if c.isalnum()
    )

```

The "problem" here is that all the `s[::-1]` and `lower()` because strings are immutable in Python, so we have some space complexity, but the solution itself. Also when using this revesrse and lower case operation I am not sure how to estimate for those builtins (can make assumptions). LC subsmission beats 33.44 in time

## Complexity


### Time: O(n)

All of the ops are casted not nested so its `O(n)`, the issue that big o notation does not consider we do multiple passes to join, lower, reverse and filter.

### Space: O(n)

Space complexity also depends on the string for the copies we create.

## Learnings


This, althought seems pretty and optimal is another clear case of using an opposite two pointer, where we dont create copies of the data and do a single pass, so time complexity is the same but space goes down to `O(1)`.

The `solution_2` is a bit even more unreadable, I messed up at the beginning and skipped some of the two pointer rules like just moving ideally one pointer at a time but was easy to figure out and the `O(1)` on space advantage.
