class Solution:
    def romanToInt(self, s: str) -> int:
        char_map = {"IV": 4, "IX": 9, "XL": 40,  "XC": 90, "CD": 400, "CM": 900,
                    "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        value = 0

        while len(s):
            if s[0:2] in char_map.keys():
                value += char_map[s[0:2]]
                s = s[2:]
            else:
                value += char_map[s[0]]
                s = s[1:]
        return value