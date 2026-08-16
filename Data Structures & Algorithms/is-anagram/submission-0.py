class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n1,n2 = len(s), len(t)
        if n1 == n2:
            if sorted(s) == sorted(t):
                return True
        return False
    
