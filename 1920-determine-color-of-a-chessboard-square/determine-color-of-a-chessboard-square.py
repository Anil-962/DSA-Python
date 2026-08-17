class Solution:
    def squareIsWhite(self, c: str) -> bool:
        column = ord(c[0])-ord('a')+1
        row =int(c[1])
        if((column+row)%2==0):
            return False
        else:
            return True
        