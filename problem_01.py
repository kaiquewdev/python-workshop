'''Python workshop: Problem 01'''

for n in range(1,10+1):
  if not n % 3:
    print("Fizz")
  elif not n % 5:
    print("Buzz")
  else:
    print(n)

