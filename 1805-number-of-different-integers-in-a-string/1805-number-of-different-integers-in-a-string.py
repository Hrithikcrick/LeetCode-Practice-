class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        nums=set()
        i=0
        while i < len(word):
            if word[i].isdigit():
                num=" "
                while i < len(word) and word[i].isdigit():
                    num+=word[i]
                    i+=1
                nums.add(int(num))
            else:
                i+=1
        return len(nums)


            
            

        