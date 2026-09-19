class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr1 = nums[:n]
        arr2 = nums[n:]
        num = []

        for i in range(n):
            num.append(arr1[i])
            num.append(arr2[i])

        return num
        
        
        