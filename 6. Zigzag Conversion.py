class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s): 
            return s
        
        res = []
        step = (numRows - 1) * 2

        for i in range(numRows):
            for j in range(i, len(s), step):
                res.append(s[j])
                diag = j + step - i * 2
                if i != 0 and i != numRows - 1 and diag < len(s):
                    res.append(s[diag])
        return "".join(res)