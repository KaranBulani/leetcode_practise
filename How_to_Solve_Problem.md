# How to Solve Problem

> Follow only what is applicable. Not every section applies to every
> problem (e.g., use Dynamic Programming section only when relevant).

------------------------------------------------------------------------

## 1. Observation

### Read the problem statement

-   Reduce it into your own words
-   Read all examples carefully

### Identify key words and phrases

-   Define constraints clearly
-   What is possible?
-   What is not possible?
-   Avoid tunnel vision --- revisit assumptions

### Identify processing direction

-   Does the problem force a direction?
-   If multiple directions exist, pick simplest or optimal

### Core Idea

-   Problem solving is NOT pure pattern matching
-   Observation is the most important skill
-   Write down observations to avoid rethinking

------------------------------------------------------------------------

## 2. Simulation

### Work through an example

-   Write decisions step-by-step
-   Choose a starting point
-   Identify actions
-   Identify consequences
-   Simulate just enough to detect structure

### Generalize

-   Replace values with variables
-   Move from example → general case

### Core Idea

-   Observations → Structure
-   Let structure guide technique instead of guessing

------------------------------------------------------------------------

## 3. Recursion (Use only if applicable)

### Build recurrence relation

-   Base case
-   Actions → Recursive calls
-   Consequences → Transitions
-   Contributions → Return values
-   Parameters → Affected variables

### Rules of recursion

1.  Base cases must be correct
2.  Recursive calls must shrink toward base case
3.  Assume recursion works correctly

### Tips

-   Name functions by what they promise
-   Avoid simulating deeply
-   Think inductively

### When to use recursion

-   Subproblems have same structure
-   Problem naturally breaks into smaller pieces

------------------------------------------------------------------------

## 4. Dynamic Programming (Use only if applicable)

### Requirements

-   Must have recurrence relation
-   Function must be pure (no side effects)

### Time Complexity

-   (# Unique States) × (Work per state)

### Key Ideas

-   DP = caching decisions
-   Compute each state once, state should be bool if it's a `Yes/No` decision, or complex datatype like `int` if needed.
-   Minimize parameters
-   Optimize transitions

### Important distinction

-   Recurrence relation != recursion
-   DP evaluates recurrence efficiently

------------------------------------------------------------------------

## 5. Technique Selection

### Flow

Observation → Properties → Structure → Technique

### Key mindset

-   Don't guess technique
-   Let structure reveal it

------------------------------------------------------------------------

## Final Notes

-   Not every problem needs all steps
-   Apply only relevant sections
-   Focus on clarity of thinking over memorization

Example

