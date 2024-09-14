class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            if len(flowerbed)==1 and flowerbed[i]==0:
                count += 1
            elif i==0:
                if flowerbed[i] == 0 and flowerbed[i+1]==0:
                    flowerbed[i] = 1
                    count += 1
            elif i==(len(flowerbed)-1):
                if flowerbed[i] == 0 and flowerbed[i-1]==0:
                    flowerbed[i] = 1
                    count += 1
                    print("this is running")
            elif flowerbed[i] == 0 and i!=(len(flowerbed)-1):
                l = flowerbed[i-1]
                r = flowerbed[i+1]
                if l == 0 and r == 0:
                    flowerbed[i] = 1
                    count += 1
            print(count)
        return count>=n if count >= n else False