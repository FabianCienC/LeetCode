## Dynamic Programing
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0: return ""

        dp = [[False] * n for _ in range(n)]

        start = 0
        maxLenght = 0

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if j - i <= 1 or dp[i+1][j-1]:
                        dp[i][j] = True

                        if j - i + 1 > maxLenght:
                            maxLenght = j - i + 1
                            start = i
        return s[start:start+maxLenght]
    
## Expand around center
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0: return ""
        
        start, end = 0, 0

        for i in range(n):
            lenEven = self.expand(s, i, i)
            lenOdd = self.expand(s, i, i+1)

            maxLenght = max(lenEven, lenOdd)

            if maxLenght > end - start + 1:
                start = i - (maxLenght - 1) // 2
                end = i + (maxLenght ) // 2
        return s[start : end + 1]
            

    def expand(self, s: str, left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
    
## Manchester
class Solution:
    def longestPalindrome(self, s: str) -> str:
        m = Manchester(s)
        n = len(s)

        maxLenght = 1
        start = 0

        for i in range(n):
            oddLen = m.getLongest(i, 1)
            if oddLen > maxLenght:
                maxLenght = oddLen
                start = i - maxLenght // 2

            evenLen = m.getLongest(i, 0)
            if evenLen > maxLenght:
                maxLenght = evenLen
                start = i - maxLenght // 2 + 1
        return s[start : start + maxLenght]

class Manchester:
    def __init__(self, s: str):
        self.ms = "@"
        for c in s:
            self.ms += "#" + c
        self.ms += "#$"

        self.p = [0] * len(self.ms)
        self.run()
    
    def run(self):
        n = len(self.ms)
        l = r = 0

        for i in range(1, n - 1):
            mirror = l + r - i

            if i < r:
                self.p[i] = min(r-i, self.p[mirror])
            
            while self.ms[i + self.p[i] + 1] == self.ms[i - self.p[i] - 1]:
                self.p[i] += 1
            
            if i + self.p[i] > r:
                l = i - self.p[i]
                r = i + self.p[i]
    
    def getLongest(self, center, odd):
        pos = 2 * center + 2 + (0 if odd else 1)
        return self.p[pos]
    
    def check(self, l, r):
        lenght = r - l + 1
        center = (r + l) // 2
        return lenght <= self.getLongest(center, lenght % 2)