class Solution:
    def romanToInt(self, s: str) -> int:
        roman_mins = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        res, prev = 0, 0
		
        for a in s[::-1]:
            if roman_mins[a] >= prev:
                res += roman_mins[a]
            else:
                res -= roman_mins[a]
            prev = roman_mins[a]
        return res

a = Solution()
print(a.romanToInt("LVIII"))