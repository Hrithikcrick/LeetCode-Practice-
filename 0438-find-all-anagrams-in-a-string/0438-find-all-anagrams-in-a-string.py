class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        n=len(p)
        need={}
        ans=[]
        for ch in p:
            need[ch]=need.get(ch,0)+1
        window={}
        left=0
        for right in range(len(s)):
            window[s[right]]=window.get(s[right],0)+1
            while right - left + 1>n:
                window[s[left]]-=1
                if window[s[left]]==0:
                    del window[s[left]]
                left+=1
            if right-left+1==n:
                if window==need:
                    ans.append(left)
        return ans