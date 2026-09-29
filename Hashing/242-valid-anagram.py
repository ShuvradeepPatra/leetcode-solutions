# LeetCode 242 - Valid Anagram
#
# Approach:
# Use a hash map to count the frequency of each character in s.
# Decrease the count for each character in t.
# If all final counts are zero, the strings are anagrams.
#
# Time Complexity: O(n)
# Space Complexity: O(k), where k is the number of distinct characters.

class Solution(object):
    def isAnagram(self, s, t):
         if len(s) != len(t):
             return False
             
         count = {}
         for ch in s:
              if ch in count:
                  count[ch]+= 1
              else:
                   count[ch] = 1
                   
         for ch in t:
              if ch in count:
                  count[ch]-= 1
              else:
                   return False
                   
         for values in count.values():
              if values != 0:
                  return False
               
         return True
