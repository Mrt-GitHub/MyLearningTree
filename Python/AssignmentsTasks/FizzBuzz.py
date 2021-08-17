'''
Opened: Tuesday, 10 August 2021, 5:00 PM
Due: Monday, 16 August 2021, 5:00 PM

Task : Print the Fizz Buzz numbers.

Fizz Buzz is a famous code challenge used in interviews to test basic programming skills. It's time to write your own implementation.
Print numbers from 1 to 100 inclusively following these instructions:
if a number is multiple of 3, print "Fizz" instead of this number,
if a number is multiple of 5, print "Buzz" instead of this number,
for numbers that are multiples of both 3 and 5, print "FizzBuzz",
print the rest of the numbers unchanged.
Output each value on a separate line.
'''

def fizz_buzz(num):
  return ['FizzBuzz' if not n%15 else 'Buzz' if not n%5 else 'Fizz' if not n%3 else n for n in range(1,num+1)]
print(fizz_buzz(100))