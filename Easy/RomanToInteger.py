"""Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        rom = {"I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000}
        
        ans = 0
        for i in range(len(s)): # 0 to len(s)-1
            #if current index is smaller than the total index and if current roman value is smaller than the next roman value, subtract ans to rom[s[i]]
            # for cases like IV, IX, XL, XC, CD, CM
            if i < len(s) - 1 and rom[s[i]] < rom[s[i+1]]:
                ans = ans - rom[s[i]]
            #else add ans to rom[s[i]]
            else:
                ans = ans + rom[s[i]]
        return ans
            
# print(rom["X"])

# MCMXCIV
# len(s)-1 = 6
# #M     
# i = 0, rom[s[i]] = 1000, rom[s[i+1]] = 100
# ans = ans + 1000 = 1000

# #C
# i = 1, rom[s[i]] = 100, rom[s[i+1]] = 1000
# ans = ans - 100 = 900

# #M
# i = 2, rom[s[i]] = 1000, rom[s[i+1]] = 10
# ans = ans + rom[s[i]] = 1900

# #X
# i = 3, rom[s[i]] = 10, rom[s[i+1]] = 100
# ans = ans - rom[s[i]] = 1900 - 10 = 1890

# #C
# i = 4, rom[s[i]] = 100, rom[s[i+1]] = 1
# ans = ans + rom[s[i]] = 1890 + 100 = 1990

# #I
# i = 5, rom[s[i]] = 1, rom[s[i+1]] = 5
# ans = ans - rom[s[i]] = 1990 - 1 = 1989

# #V
# i = 6, rom[s[i]] = 1, rom[s[i+1]] = 5
# ans = ans + rom[s[i]] = 1989 + 5 = 1994