## How to know DP is applicable here:

---
🧠 Why DP doesn’t come to mind (your exact issue)

What you described:

> “I start trying combinations / alternatives and get stuck in brute force”

That’s actually **perfect** — because DP is literally:

👉 *Optimizing brute force recursion*

So the issue is NOT that you don’t know DP. The issue is:

👉 You’re not recognizing that your brute force is **recomputing the same thing**

---
🔍 The mental trigger for DP

Whenever you see a problem, ask this:

❓ “If I try all possibilities, will I recompute the same subproblem again?”

If YES → 🚨 **DP problem**

---
🧩 Step-by-step recognition framework

Use this every time:

---
1. Can I define the problem in terms of choices?

Example (House Robber):
* At index `i`, I have 2 choices:
  * rob → go to `i+2`
  * skip → go to `i+1`

👉 If problem = *sequence of choices* → strong DP candidate

---
2. Does the problem ask for optimization?

Look for keywords:
* max / min / count / ways

👉 Optimization + choices = **DP almost always**

---
3. Can I write a recursive relation?

Try forcing yourself:
```
f(i) = best answer starting from index i
```

If you can express:
```
f(i) = max(
    nums[i] + f(i+2),
    f(i+1)
)
```
👉 BOOM — this is DP

---
4. Will recursion repeat work?

Draw a small recursion tree:

For House Robber:
```
f(0)
 ├── f(2)
 │    ├── f(4)
 │    └── f(3)
 └── f(1)
      ├── f(3)  <-- repeated!
      └── f(2)  <-- repeated!
```
👉 Same states → repeated work → DP

---
🚨 Why you’re defaulting to brute force

You’re doing this:
> “Try combinations”

That means you’re thinking:

👉 *subsets / permutations mindset*

Instead, switch to:

👉 *state transition mindset*

---
🔄 Shift your thinking (this is the key)

❌ Wrong mindset (what you're doing)

“Let me try all combinations of houses”

✅ Correct DP mindset

“At each index, what’s the best I can do?”

---
🧠 Golden DP template (burn this in your brain)

Whenever stuck, force this:
```
1. Define state:
   f(i) = answer starting from i

2. Define choices:
   take / not take

3. Write recurrence:
   f(i) = best of choices

4. Add memoization
```

---
🧪 Quick test: DP or NOT?

Ask these 5 questions:

| Question                            | If YES         |
| ----------------------------------- | -------------- |
| Is it optimization (max/min/count)? | → DP likely    |
| Do I have choices at each step?     | → DP likely    |
| Can I define a state like f(i)?     | → DP likely    |
| Will recursion repeat states?       | → DP confirmed |
| Is greedy failing?                  | → DP likely    |

---
⚡ Compare with NON-DP problems

❌ Binary Search
* No overlapping subproblems
* No repeated work

❌ Two Pointers
* Linear progression
* No branching choices

❌ Sliding Window
* Expanding/shrinking window
* No recursion

👉 These don’t have **branching + overlap**

---
🧠 The real trick (most important)

Next time you solve:

👉 **DON’T jump to DP immediately**

Instead:
1. Write brute force recursion
2. Draw recursion tree (small input)
3. Spot repetition

👉 That’s when DP should “click”

---
🔥 Practice trick (this will fix your issue fast)

For next 10 problems:
* ALWAYS start with recursion
* Even if you know DP

Then ask:
> “Which calls are repeating?”

👉 That moment = DP intuition

---
🎯 Final takeaway

You don’t “recognize DP” at the start.

👉 You **discover DP after writing recursion**

---
## How to convert top down approach to bottom up tabulation

---
🧠 1. Identify the DP state

In top-down (memoization), you usually have:
```python
def dfs(i, ...):
    if base_case:
        return value
    if memo[i] exists:
        return memo[i]
    
    memo[i] = recurrence
    return memo[i]
```
👉 Your **DP state = function parameters**

---
🧮 2. Write the recurrence clearly

Example:

```python
dp[i] = max(dp[i-1], nums[i] + dp[i-2])
```

👉 This is the *most important step*

If you can’t write recurrence → you can’t tabulate

---
📦 3. Decide table structure

From parameters:

| Top-down param | Bottom-up table |
| -------------- | --------------- |
| `i`            | `dp[i]`         |
| `i, j`         | `dp[i][j]`      |

---
🚦 4. Handle base cases FIRST

Whatever base case in recursion → initialize in table

Example:

```python
if i == 0: return nums[0]
```

becomes:

```python
dp[0] = nums[0]
```

#### Various pattern of base cases:

_Pattern 1: Counting Ways Problems_

In problems like:
* Combination Sum IV
* Coin Change II
* Target Sum

`dp[i]` usually means:
> “number of ways to form amount i”

Then:
```python
dp[0] = 1
```

because:
> there is ONE way to make amount 0
> 
> → choose nothing

This act as contribution of one COMPLETE valid path

Example:

If:
```python
dp[2] += dp[0]
```

that means:
> “Using this coin directly forms amount 2.”

If `dp[0]` were `0`, nothing would ever start.

_Pattern 2: Optimization Problems (min/max)_

In problems like:
* Coin Change (minimum coins)
* Perfect Squares
* Min Cost Climbing Stairs

`dp[i]` means something like:
> minimum operations/cost/items needed to reach i

Then `dp[0]` is often:
```python
dp[0] = 0
```

because:
> it takes 0 coins to make amount 0

Example:

```python
dp[x] = min(dp[x], dp[x-coin] + 1)
```

If:

```python
x == coin
```

then:

```python
dp[coin] = dp[0] + 1 = 1
```

which is correct.

_Pattern 3: Boolean Reachability Problems_

In problems like:

* Word Break
* Partition Equal Subset Sum
* Can Sum

`dp[i]` means:

> “Is state i reachable?”

Then:

```python
dp[0] = True
```

because:

> empty state is achievable trivially



_Quick Mental Rule_

Before writing base case, ask:

> “What does dp[i] represent?”

Then plug in:

```text
What should dp[0] mean under that definition?
```

That automatically gives the correct base case.

---
🔄 5. Decide iteration order

You must compute states **before they are needed**

Ask:
> "What does dp[i] depend on?"

Example:
* depends on `i-1`, `i-2`

  👉 Then iterate forward

```python
for i in range(2, n):
```
---
🧱 6. Fill the table

Convert recursion → loop

---
🔥 Example: House Robber 

🧠 Top-down

```python
def dfs(i):
    if i >= n:
        return 0
    
    if i in memo:
        return memo[i]
    
    rob = nums[i] + dfs(i+2)
    skip = dfs(i+1)
    
    memo[i] = max(rob, skip)
    return memo[i]
```
---
🔁 Convert to Bottom-up

Step 1: State

`dfs(i)` → `dp[i]`

---
Step 2: Meaning

`dp[i] = max money from index i → end`

---
Step 3: Base case

```python
dp[n] = 0
dp[n+1] = 0
```
---
Step 4: Direction

`dp[i]` Depends on `i+1`, `i+2`

👉 go **backwards**

---
Step 5: Code

```python
n = len(nums)
dp = [0] * (n + 2)

for i in range(n - 1, -1, -1):
    rob = nums[i] + dp[i + 2]
    skip = dp[i + 1]
    dp[i] = max(rob, skip)

return dp[0]
```

---
⚡ Think:

✅ "What does dp[i] represent?"

Once you define meaning clearly → tabulation becomes mechanical

---
🧩 Patterns You’ll See Often

1. Forward DP

```python
dp[i] depends on dp[i-1]
```

→ loop from `0 → n`

---
2. Backward DP

```python
dp[i] depends on dp[i+1]
```

→ loop from `n-1 → 0`

---
3. 2D DP

```python
dp[i][j] depends on dp[i-1][j], dp[i][j-1]
```

→ nested loops

---
🚨 Common Mistakes

* ❌ Wrong loop direction
  * ❌ Missing base case initialization
  * ❌ Using recursion logic directly without redefining meaning
  * ❌ Not allocating extra space (`n+1`, `n+2`)

---
💡 Final Mental Model

Whenever you see recursion:
1. Replace function → array
2. Replace calls → indices
3. Replace return → assignment
4. Replace call stack → loop order


---
## Converting Recursion to Top-Down DP (Memoization)

---

### Problem with Plain Recursion

In normal recursion, the same states are computed repeatedly.

For this problem, a recursive state is:
dfs(i, curr_target)

Meaning:
* i → current index
* curr_target → remaining target we still need to form

Without memoization, many identical (i, curr_target) states are recalculated.

---

### Step-by-Step Conversion Process

---

#### Step 1: Identify the Recursive State

Look for the variables changing between recursive calls.

In this recursion:
```python
dfs(i + 1, curr_target - nums[i])
dfs(i + 1, curr_target + nums[i])
```

the changing variables are:
* i
* curr_target

So the DP state becomes:
(i, curr_target)

---

#### Step 2: Convert Side-Effect Recursion into Return-Based Recursion

_Original Approach_

The original recursion uses a global variable: `res += 1`

This is harder to memoize cleanly.

_DP-Friendly Approach_

Instead of modifying a global variable:
> Let the recursive function RETURN the number of ways.

So: `dfs(state)`

should mean:
> "How many valid ways exist from this state?"

#### Step 3: Rewrite the Base Case

_Original Base Case_
```python
if i == len(nums) and curr_target == 0:
    res += 1
```

_DP Base Case_
```python
if i == len(nums):
    return 1 if curr_target == 0 else 0
```

Meaning:
* If all numbers are used and target becomes 0
  → one valid expression found
* Otherwise
  → no valid expression
---
#### Step 4: Return Recursive Answers

_Original Recursion_
```python
dfs(i+1, curr_target - nums[i])
dfs(i+1, curr_target + nums[i])
```

_DP Recursion_

Each recursive call returns number of valid ways:

```python
return (
    dfs(i+1, curr_target - nums[i]) +
    dfs(i+1, curr_target + nums[i])
)
```
---
#### Step 5: Add Memoization

Store already computed states:
```python
memo[(i, curr_target)] = answer
```

Before computing:

```python
if (i, curr_target) in memo:
    return memo[(i, curr_target)]

```
This avoids recomputation.

---

#### Core Mindset Shift

_Plain Recursion_
> “Do some work globally”

Uses: `res += 1`

_Top-Down DP_

> “This function RETURNS the answer for this state”

That is the key idea behind memoization.

---

#### General Recipe: Recursion → Top-Down DP

Whenever converting recursion into DP:

1. Find changing variables. These become DP state variables.
2. Make recursion return answers. Avoid global variables whenever possible.
3. Cache computed states `memo[state] = answer`
---