class Solution:
    def isAnagram(self, s: str, t: str):
        f1, f2 = {}, {}

        if len(s) != len(t):
            return False

        for i in s:
            f1[i] = f1.get(i,0)+1

        for j in t:
            f2[j] = f2.get(j,0)+1

        
        for num in f1:
            if f1[num]  != f2.get(num, 0):
                return False
        
        return True



    
