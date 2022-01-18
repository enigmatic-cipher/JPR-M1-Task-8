"""
Given x and n as input, print the sum of x1 + x2+....+xn
Input -> n=3, x=10
Output -> 1110 (because 1110 = 10+100+1000)
"""

x = 10
n = 3
total = 0
for i in range(1,n+1):
  total = total + x**i
print(total)
