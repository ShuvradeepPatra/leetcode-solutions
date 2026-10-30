# LeetCode 1 — Two Sum

## Approach: Brute Force

We use two nested loops to check every possible pair of elements in the array.

1. The outer loop selects the first element.
2. The inner loop selects the next elements.
3. If the sum of both elements equals the target, return their indices.

## Python Solution

```python
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return -1
```

## Complexity Analysis

- **Time Complexity:** O(n²) — Nested loops check possible pairs.
- **Space Complexity:** O(1) — No additional data structure is used.

## Approach Summary

This is the brute-force approach. It is straightforward but can be optimized using a Hash Map to achieve O(n) time complexity.
