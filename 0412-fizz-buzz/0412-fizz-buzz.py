class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        answer = []
        position = 1
        while position <= n:
            if ((position % 3 == 0) and (position % 5 == 0)):
                answer.append("FizzBuzz")
            elif ((position % 3 == 0) and (position % 5 != 0)):
                answer.append("Fizz")
            elif ((position % 3 != 0) and (position % 5 == 0)):
                answer.append("Buzz")
            else:
                answer.append(str(position))
            position = position + 1
        return answer
        