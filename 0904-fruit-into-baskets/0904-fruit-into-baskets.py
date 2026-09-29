class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        left = 0
        freq={}
        maxi=0
        for right in range(len(fruits)):
            freq[fruits[right]]=freq.get(fruits[right],0)+1
            if len(freq)>2:
                freq[fruits[left]]-=1
                if freq[fruits[left]]==0:
                    del freq[fruits[left]]
                left+=1
            maxi=max(maxi,right-left+1)
        return maxi
        