### 1. **Greedy Algorithms**

- **How They Work:** Greedy algorithms make the locally optimal choice at each step, hoping to find the global optimum. They are often suitable when the problem has a "greedy choice property," meaning a locally optimal choice leads to a globally optimal solution.
- **Example:** In the coin change problem, a greedy algorithm might select the largest coin denomination first, then the next largest, and so on.
- **Limitations:** Greedy algorithms don't always provide the optimal solution for all problems. For example, if you have coins of denominations 1, 3, and 4, and you want to make 6, the greedy approach might select two 3-coin pieces, missing the optimal solution of using two 1-coin pieces and one 4-coin piece.

### 2. **Dynamic Programming (DP)**

- **Principles:** DP solves problems by breaking them down into overlapping subproblems, solving each subproblem only once, and storing their solutions. It's suitable for problems that have an optimal substructure, where the solution to a problem can be constructed from the solutions to its subproblems.
- **Coin Change Problem:** Use DP to find the minimum number of coins needed to make a certain amount. You'll create a list where each index represents an amount, and the value at that index represents the minimum number of coins needed to make that amount.
- **Example in Python:**
  ```python
  def coinChange(coins, amount):
      dp = [float('inf')] * (amount + 1)
      dp[0] = 0

      for coin in coins:
          for x in range(coin, amount + 1):
              dp[x] = min(dp[x], dp[x - coin] + 1)

      return dp[amount] if dp[amount] != float('inf') else -1
  ```

### 3. **Algorithmic Complexity**

- **Time Complexity:** Analyze how the runtime of your algorithm increases with the input size. For the dynamic programming solution to the coin change problem, the time complexity is `O(n * amount)`, where `n` is the number of different coins.
- **Space Complexity:** Understand how much memory your algorithm uses. The DP solution uses `O(amount)` space.

### 4. **Problem-Solving Strategies**

- **Breaking Down Problems:** For complex problems like coin change, divide them into smaller subproblems (e.g., finding the minimum coins needed for each smaller amount up to the target amount).
- **Iterative vs. Recursive DP:** Iterative DP often uses less memory because it avoids the overhead of recursive calls.

### 5. **Python Programming**

- **Lists and List Comprehensions:** In the DP solution, you'll manipulate lists (e.g., the `dp` list).
- **Efficient Looping and Conditionals:** Use loops and conditionals to update your DP table effectively.

---

**Example Interview Question: Coin Change Problem**

Given a list of coin denominations and a target amount, find the minimum number of coins needed to make that amount. If it's not possible to make the amount, return -1.

**Example Input:**

```python
coins = [1, 2, 5]
amount = 11
```

**Expected Output:**

```python
3  # (11 = 5 + 5 + 1)
```
