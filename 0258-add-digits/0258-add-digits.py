class Solution:
    def addDigits(self, num: int) -> int:
        digit=0
        
        while num>=10:
            while num:
                digit+=num%10
                num=num//10
            num=digit
            digit=0
        return num


        