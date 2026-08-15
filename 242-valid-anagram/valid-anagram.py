class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sort_s=sorted(s)
        sort_t=sorted(t)
        if sorted(s)==sorted(t):
            return True
        return False    
        
        