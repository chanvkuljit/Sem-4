'''
14.Write a program to print all prime numbers between 1 to 100.
'''

for num in range(1,100+ 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
