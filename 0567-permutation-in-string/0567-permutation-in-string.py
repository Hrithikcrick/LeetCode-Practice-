class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n=len(s1)
        if n > len(s2):
            return False
        need={}
        for ch in range(len(s1)):
            need[s1[ch]]=need.get(s1[ch],0)+1
        window={}
        left=0
        for right in range(len(s2)):
            window[s2[right]]=window.get(s2[right],0)+1
            if right - left + 1 > n:
                window[s2[left]]-=1
                if window[s2[left]]==0:
                    del window[s2[left]]
                left+=1
            if right-left+1==n:
                
                if window==need:
                    return True
        return False
        