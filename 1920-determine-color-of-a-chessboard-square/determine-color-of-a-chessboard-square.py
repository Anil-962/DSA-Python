class Solution:
    def squareIsWhite(self, c: str) -> bool:
        if c[0] in "acge":
            if c[1] in "1357":
                return False
            else:
                return True
        else:
            if c[1] in "2468":
                return False
            else:
                return True
        