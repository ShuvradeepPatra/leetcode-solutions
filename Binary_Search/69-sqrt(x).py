# LeetCode 69 — Sqrt(x)

## Approach: Binary Search

We use binary search to find the integer square root of `x`.

1. Initialize `left = 0` and `right = x`.
2. Calculate the middle value.
3. If `mid * mid == x`, return `mid`.
4. If `mid * mid > x`, search the left half.
5. Otherwise, search the right half.
6. When the loop ends, return `right`, which represents the floor of the square root.

## Python Solution

```python
class Solution(object):
    def mySqrt(self, x):
        left = 0
        right = x

        while left <= right:
            mid = (left + right) // 2

            if mid * mid == x:
                return mid
            elif mid * mid > x:
                right = mid - 1
            else:
                left = mid + 1

        return right
```

## Complexity Analysis

- **Time Complexity:** O(log x) — The search space is halved in every iteration.
- **Space Complexity:** O(1) — Only a constant amount of extra memory is used.

## Key Concept

Binary search efficiently finds the largest integer `k` satisfying:

`k * k <= x`

The final value of `right` is the integer square root.
