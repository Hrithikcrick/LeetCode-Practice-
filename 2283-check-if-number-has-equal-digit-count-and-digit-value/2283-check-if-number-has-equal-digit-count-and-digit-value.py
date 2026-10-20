class Solution:
    def digitCount(self, num: str) -> bool:
        freq = {}
        arr = list(map(int, num))

        for x in arr:
            freq[x] = freq.get(x, 0) + 1

        for i in range(len(num)):
            if arr[i] != freq.get(i, 0):
                return False

        return True
  
            
            