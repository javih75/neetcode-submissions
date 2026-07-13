class Solution:
    def countBits(self, n: int) -> List[int]:
        lst = []
        for i in range(n+1):
            countOnes = 0
            x = i
            y = i % 2
            while x > 0:
                if y == 1:
                    countOnes += 1
                x = x // 2
                y = x % 2
            lst.append(countOnes)
        return(lst)