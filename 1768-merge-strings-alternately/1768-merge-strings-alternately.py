class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        char1=list(word1)
        char2=list(word2)
        ans=[]
        i=0
        j=0
        while i<len(char1) and j < len(char2):
            ans.append(char1[i])
            ans.append(char2[j])
            i+=1
            j+=1
        if i != len(char1):
            for k in range(i,len(char1)):
                ans.append(char1[k])
        if j != len(char2):
            for k in range(j,len(char2)):
                ans.append(char2[k])
        ans="".join(ans)
        return ans
            

        