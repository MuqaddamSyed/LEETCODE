#345_Reverse Vowels of a String.py
class Solution:
    def reverseVowels(self, s: str) -> str:
        # 1. Define vowels in a set for O(1) lookup
        vowels = set("aeiouAEIOU")
        
        # 2. Convert to list since strings are immutable
        chars = list(s)
        
        # 3. Initialize pointers at both ends
        left, right = 0, len(s) - 1
        
        while left < right:
            # Move left pointer until it finds a vowel
            while left < right and chars[left] not in vowels:
                left += 1
            
            # Move right pointer until it finds a vowel
            while left < right and chars[right] not in vowels:
                right -= 1
            
            # 4. Swap vowels and move pointers inward
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
            
        # 5. Join list back into a string
        return "".join(chars)
