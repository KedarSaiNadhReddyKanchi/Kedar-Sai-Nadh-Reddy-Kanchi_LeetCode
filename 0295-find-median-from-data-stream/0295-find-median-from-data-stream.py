class MedianFinder:

    def __init__(self):
        self.hashmap = {}
        self.count = 0
        self.numbers = []
        

    def addNum(self, num: int) -> None:
        if len(self.numbers) == 0:
            self.numbers.append(num)
        elif len(self.numbers) == 1:
            if num >= self.numbers[0]:
                self.numbers.append(num)
            else:
                temp = self.numbers[0]
                self.numbers.append(temp)
                self.numbers[0] = num
        else:
            position = 0
            for number in self.numbers:
                if number > num:
                    break
                position = position + 1
            # print("position - " , position)
            self.numbers.insert((position), num)
        
        self.count = self.count + 1
                
        

    def findMedian(self) -> float:
        if self.count % 2 == 0:
            # the total number of elements in the data stream is even
            firstMid = int(self.count / 2)
            secondMid = firstMid - 1
            # print(self.numbers)
            num1 = self.numbers[firstMid]
            num2 = self.numbers[secondMid]
            sumOfTwoNums = num1 + num2
            median = sumOfTwoNums / 2
            # print(num1 , " " , num2 , " " , sum , " " , median)
            return median
        else:
            # the total number of elements in the data stream is odd
            mid = int(self.count / 2)
            # print(mid , " " , self.count)
            return self.numbers[mid]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()