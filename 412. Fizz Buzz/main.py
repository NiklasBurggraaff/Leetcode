from ast import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        def val(i: int):
            if i % 15 == 0:
                return "FizzBuzz"
            elif i % 3 == 0:
                return "Fizz"
            elif i % 5 == 0:
                return "Buzz"
            else:
                return str(i)

        return [val(i) for i in range(1, n+1)]
