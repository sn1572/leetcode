class Solution:
    def fizzBuzz(self, n: 'int') -> 'List[str]':
        i = 1
        out = []
        while i<n+1:
            if i%15 == 0:
                out.append('FizzBuzz')
            elif i%5 == 0:
                out.append('Buzz')
            elif i%3 == 0:
                out.append('Fizz')
            else:
                out.append(str(i))
            i = i+1
        return(out)