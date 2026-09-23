class Solution:
    def greatestLetter(self, s: str) -> str:
        lows = [False] * 26
        caps = [False] * 26
        ret = ""
        for c in s:
            if c >= 'a' and c <= 'z':
                lows[ord(c) - ord('a')] = True
                if caps[ord(c.upper()) - ord('A')] and c.upper() > ret:
                    ret = c.upper()
            else:
                caps[ord(c) - ord('A')] = True
                if lows[ord(c.lower()) - ord('a')] and c > ret:
                    ret = c
        
        return ret
