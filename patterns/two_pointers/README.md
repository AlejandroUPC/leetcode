# Pattern: Two Pointers

## 1. Definition

Use of two indices (pointers) to traverse a data structure(most likely an array or str) instead of one, adds some complexity but might save you additional recursions, the end goal is to:
- reduce unnecesary comparisions
- avoid nested loops
- linear time complexity

One of the key ideas is the pair-comparision, instead of having to loop twice to get the pairs at `O(n^2)` we play around with pointers at `O(n)`.

---

## 2. Intuition 
The brutte force approach to compare all of the items in an array `[1, 2, 3, 4, 6]` could be:

- Compare 1 with all others
- Compare 2 with all others 
- etc ...

This way we repeat work constantly, but if we use two pointers approach we can:

- Look at the extrems (start-end)
- Use any information we have to eliminate possibilites

One of the core intuitions is that we can eliminate a lot (hopefully) of the search space by inteligently moving the pointers.

Two pointers though is easier to understand when used in a sorted array (not always the case) as then whether moving left or right, gives some meaning to the direction.

---

## 3. Core Mechanism

The mechanism is quite simple:

### Step 1: Init the pointers

```markdown
left = 0
right = n - 1
```


### Step 2: Compare

Do the custom logic to evaluate both pointers:

- Key components:
  - value `left` and `right`
  - a condition determines progress (sum, equaliyt, ordering, ...)

- General process:
  1. Initialize pointers
  2. Evaluate both pointers' values
  3. Move one pointer based on logic
  4. Repeat until pointers meet or condition is staisfied

**Critical detail**: Typically try to move just one pointer at a time, two might be risky.

---

## 4. Preconditions / Requirements

Conditions under which the pattern is applicable:

- There is a structure in the data (sorted order, symmetry, monotonic behaviour...)
- There is a clear rule on how to move the pointers deterministically
- Moving a pointer means eliminating a part of the search space safely

---

## 5. Recognition Signals

Indicators that suggest this pattern may apply:

- Problems involving pairs or triplets.
- Brute force solution has nested loops.
- The input is either sorted or can be sorted.
- You have to optimizze comparisions or reduce time complexity.
- Ther eis a range that can be shrunk in the progress.

---

## 6. Variants

Different forms or adaptations of the pattern:

### 1. Opposite Direction Pointers

- One pointer at the start/end
- Move inward

Used for:

- pair problems
- optimization (min/max)

### 2. Same Direction (Fast/Slow)

- Both pointers move same direction
- One moves faster or tracks position

Used for:

- filtering/partitioining
- in-place modifications

### 3. Sliding Window (Dynamic two pointers)

- Both pointers define a window
- Expand and shrink dynamically

Used for:

- contiguous subarray problems

### 4. Relative Speed (cycle detection)

- Pointers move at different speeds

Used for:

- Linked list cycle detection

---

## 7. Complexity Characteristics

Typical complexity expectations:

- Time Complexity: O(n): Each pointers should at most move `n` times, **no pointer ever moves backwards** and the total ops are linear, not multiplicable.
- Space Complexity: O(1): No additional data structures are requiered.


---

## 8. Trade-offs

Advantages:

- Reduce cuadratic problems to linear time.
- Simple and efficient.
- Works in-place (mem efficient).

Limitations:

- Most of the time needs to be sorted or structured data.
- Not applicable when deceissions can't eliminate possibilities.
- Easy to misuse if movement of pointers logic is unclear.

---

## 9. Common Mistakes

Frequent conceptual or implementation errors:

- Moving pointers without a clear rule.
- Moving both pointers at once (w/o clear justification).
- Applying without the right strucute (unsorted when data order matters).
- Miss edge cases.
- Breakin invariant that guarantees correctness.

---

## 10. Mental Model

Concise conceptual model:

> Maintaining a nrange and shrinking it by discarding impossible candidates on each step.

---

## 11. Implementation Notes

Language-agnostic considerations:

- Edge cases:
  - Empty input
  - Single element
  - All elements equal
  - Duplicate values

- Boundary conditions:
  - Ensure pointers do not go out of bound
  - Handle `left == right` if needed

- Termination conditions:
  - When `left >= right` aka pointers meet
  - Condition satisified before the above happens

---

## 12. When Not to Use

Scenarios where this pattern is not appropriate:

- Data has no structure (ordering, symmetry, ...)
- No clear rule to eliminate candidates as we progress
- Probelm requieres checking all combinations
- Decissions are not monotonic (aka moving pointers does not lead to predictable outcomes)

---

## 13. Optional: Practice Log


### Phase 1 — Foundation
- [Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
- [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)

### Phase 2 — Reinforcement
- [Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/)
- [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)

### Phase 3 — Deeper Reasoning
- [Container With Most Water](https://leetcode.com/problems/container-with-most-water/)

### Phase 4 — Stretch
- [3Sum](https://leetcode.com/problems/3sum/)

- Observations:
  - 
- Difficulties encountered:
  - 
- Refinements to understanding:
  - 
