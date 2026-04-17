# Final Prices With a Special Discount in a Shop 

## Problem

You are given an integer array prices where prices[i] is the price of the ith item in a shop.

There is a special discount for items in the shop. If you buy the ith item, then you will receive a discount equivalent to prices[j] where j is the minimum index such that j > i and prices[j] <= prices[i]. Otherwise, you will not receive any discount at all.

Return an integer array answer where answer[i] is the final price you will pay for the ith item of the shop, considering the special discount.

 

Example 1:

Input: prices = [8,4,6,2,3]

Output: [4,2,4,2,3]

Explanation: 

- For item 0 with price[0]=8 you will receive a discount equivalent to prices[1]=4, therefore, the final price you will pay is 8 - 4 = 4.
- For item 1 with price[1]=4 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 4 - 2 = 2.
- For item 2 with price[2]=6 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 6 - 2 = 4.
- For items 3 and 4 you will not receive any discount at all.


Example 2:

Input: prices = [1,2,3,4,5]

Output: [1,2,3,4,5]

Explanation: In this case, for all items, you will not receive any discount at all.


Example 3:

Input: prices = [10,1,1,6]

Output: [9,0,1,6]


## Approach

Important to read understand, basically if you buy an item you look for the next item in the array where the price is <= than the current value of the position you are in, looks like a two pointer problem where we have a fix position we keep advancing with 1 and the next pointer at position + 1 can iterate until we find a discount, if any.

After a lot of thought, I ended up having a more complex solution and when checking responses and thinking the main take away is to append just once (I had multiple append and stuff), I think the best mental model is:

1. We need two iterations for the entire array and start+1 prev position + entire array.
2. We assume there will always be a discount, but this discount could be 0 also if we don't find a match.
3. We iterate the pairs, the first that meets condition, we set the discount to whatever the price we were comparing.
4. We substract discount (which is inited as 0 and the value is populated as we iterate) and append.


## Complexity


### Time: O(n^2)

We iterate once the entire array `n` , and for every iteration we (worst case) iterate again on `n - 1 - i` (`n-1)` because rang is not inclusive of last element and `i` because we keep reducing the array as we only look forward prices). So `O(n) * O(n-i-1)` when we remove the constants is `O(n^2)`.

### Space: O(n)

The space complexity where we store the results is constant, we just declare a variable and append `O(n)`.

## Learnings

Sometimes my head messes up with pointers when computing iterations, e.g took me a while to really wrap my head around that second loop was `n - i - 1`.

But there is also a much more efficient way to think about this, right now we go left to right and keep looping, and on every look we think: What's the first discount we can check for? Well there is this pattern called **Monotonic Stack** (Monotonig increaseing Stack by value, in this case), this should ring a bell when we see a problem that asks for:

- Next smaller element to the right
- Next greater element to the right
- Nearest smaller/greater element

### What is a monotonic stack?

Its just a in increase (similar to monotonic timers) that maintaints a specific order, e.g increasing is `[2, 4, 6, 9]` and decreaseing is `[9, 6, 4, 2]`.
Right now we are repeating this comparission many times where we keep comparing all of the current prices to potential discounts, **why can't we store the elements that are waiting for a smaller value?**.

So we think in ways that our stack is `"items waiting for their discounts"`, the following markdown snippet we break down the pseudo code:

```markdown
prices = [8, 4, 6, 2, 3]
results = [8, 4, 6, 2, 3] # init as copy of prices
stack = [] # NOTE This stores INDEXES!

## Step 1 (i = 0)

current_price = 8, stack is empty, no waiting for a discount we append 0 INDEX
stack = [0]

## Step 2 (i = 1)
current_price  = 4
is current_price <= prices[stack[-1]] # stack[-1] == 0 aka 8
if yes,8 has found a discount, 4
results[0] = 8 - 4 = 4
we clean the stack and set it to the next one as 0 already found his:
stack = []
stack = [1]

# Step 3 (i = 2)
current_price = 6
is current_price <= prices[stack[-1]] # stack[-1] == 1 aka 4
No discount, we push stack:
stack = [1, 2]

# Step 4 (i = 3)
current_price = 2
is current_price <= price[stack[-1]] # stack[-1] == 2 aka 6
Yes
result[2] = 6 - 2 = 4

And we pop stack:
stack = [1]

We check again
is current_price <= price[stack[-1]] # stack[-1] == 1 aka 4, 2<4?
2 < 4 so yes again,
result[1] = 4 - 2 = 2
stack = [] # we pop
push current:
stac = [3]

# Step 5 (i = 4)
is current_price <= price[stack[-1]] # stack[-1] == 3 aka 3, 2 <3 No
2 < 3 is false so we push
stack = [3, 4]

Loop is over, 3,4 never found a discount so they stay the same on the `result array`

result = [4, 2, 4, 2, 3]
          0  1  2  3  4  
prices = [8, 4, 6, 2, 3]

```

This is very interesting because it switches the mental model where `i` is the price we are looking to compare discounts, and `stack` is a growing list of items (pointing to the indexes) that we are looking to get discounts for, and as we go from left to right it could be that if we had an every growing stack (because we could not find any discount) when we meet a very low value the entire stack goes empty, e.g `prices = [2, 3, 4, 5, 1]`.

Here is another slightly more complex example:

```markdown
prices = [2, 5, 7, 9, 3, 8]
          0  1  2  3  4  5
discounts = prices.copy()
stack = []
We can already see that its ascending pretty much until 9 (index = 3), but then when we reach 3 (index=4) we will be able to apply discount to all the items we stacked until we 2 (condition 2 <= 3 is false).

Step 1 (i = 0):
First case, empty stack, we push:
stack = [0]

Step 2 (i = 1):
for item in stack: #pseudo code
    price[i] <= price[0]: # 5 <= 2
        no
so we add to stack, all the items in the stack (in this case just index = 0) failed to find a discount using i = 1 aka 2.
stack = [0, 1] # both 2 and 5 anre looking for discounts

Step 3 (i = 2):
for items in stack:
    price[i] <= price[1]: # 7 <= 5
        no
    price[i] <= price[0]: # 7 <= 2
        no
stack empty, no discount found, push next item
stack = [0, 1, 2]

Step 4 (i = 3):
for item in stack:
    price[i] <= price[2]: 9 <= 7 (or 5, 2 for next item to stack):
        all no,
stack = [0, 1, 2, 3]

Step 5 (i = 4)
for item in stack:
    price[i] <= price[3]: # 3 <= 9, yes!
        yes, discounts[3] = 9 - 3, and we pop stack
    price[i] <= price[2]: # 3 <= 7, yes!
        yes, discounts[2] = 4
    price[i] <= prices[1]: # 3 <= 5, yes!
        yes, discounts[1] = 2, stack pop
    price[i] <= prices[0]: # 3 <= 2, no, we keep in stack

Step 6 (i = 5):
    for item in stack:
        price[i] <= price[0]: # 8 <= 2, no, add stack
        stack = [0, 5]

End of computation, w could not find discounts for index 0 and 5.
discounts = [2, 2, 4, 6, 3, 8]
```

What we see in this example is that there is a small build up when we follow an increasing tendency (? does this even exist) and whene there is a minor value we decrease the stack.

The time complexity here changes, we are iterating once the array (and although we have a while loop w/ push and pops), worse case scenarion is we push and pop once per `i` in `n`, so `2n -> O(n)`, **amortized** (reminder that amortized is when a lot of small ops that happen more often coover up an expensive one.
Space does not change as we also just declare a copy of the array of length `n` so `O(n)`.
