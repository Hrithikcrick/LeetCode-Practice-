class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        n=len(cardPoints)
        
        window_size=n-k
        if window_size==0:
            return sum(cardPoints)
        total_sum=sum(cardPoints)
        window_sum=0
        left=0
        mini=float('inf')
        for right in range(len(cardPoints)):
            window_sum+=cardPoints[right]
            while right - left + 1>window_size:
                window_sum-=cardPoints[left]
                left+=1
            if right-left+1==window_size:
                mini=min(mini,window_sum)
        return total_sum-mini

