class Solution:
    def romanToInt(self, s: str) -> int:
        roman_mapping = {
            "M":1000,  "CM":900 , "D":500, "CD":400,
            "C":100,   "XC":90,  "L":50,  "XL":40,
            "X":10,   "IX":9,   "V":5,   "IV":4,
            "I":1
        }
        
        result =0
        n = len(s)
        for i in range(n):
            if i<n-1 and roman_mapping[s[i]]<roman_mapping[s[i+1]]:
                result -=roman_mapping[s[i]]
            else:
                result +=roman_mapping[s[i]]
        return result

        