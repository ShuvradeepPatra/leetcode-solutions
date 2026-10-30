# LeetCode 7 — Reverse Integer

## Approach: Digit Extraction

We reverse the integer by extracting its last digit and adding it to the result.

1. Initialize `ans = 0`.
2. Extract the last digit using `x % 10`.
3. Append the digit using `ans = ans * 10 + digit`.
4. Remove the last digit using `x = x / 10`.
5. Check integer overflow before updating the answer.

## C++ Solution

```cpp
class Solution {
public:
    int reverse(int x) {
        int ans = 0;

        while(x != 0) {
            int digit = x % 10;

            if((ans > INT_MAX/10) || (ans < INT_MIN/10)) {
                return 0;
            }

            ans = (ans * 10) + digit;
            x = x / 10;
        }

        return ans;
    }
};
```

## Complexity Analysis

- **Time Complexity:** O(log₁₀ |x|) — We process each digit once.
- **Space Complexity:** O(1) — Only a constant amount of extra memory is used.

## Key Concept

Integer overflow must be checked before multiplying the current answer by 10. If the reversed integer exceeds the 32-bit signed integer range, return 0.
