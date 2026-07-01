class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

            if n == 0 :
                return True
            
            length = len(flowerbed)

            for i in range(length):

                if flowerbed[i] == 0: 
                    left_emtpy = (i == 0) or (flowerbed[i - 1] == 0)
                    right_emtpy = (i == length - 1) or (flowerbed[i + 1] == 0)

                    if left_emtpy and right_emtpy:

                        flowerbed[i] = 1
                        n-=1

                        if n <=0:
                            return True

            return False




        