'''
11.Write a program to input a number and display Factorial of that 
number. For example, Factorial of 5 = 5 * 4 * 3 * 2 * 1 = 120. 
'''

num=int(input("Enter Number:"))
fact=1

for i in range(1,num+1):
    fact=fact*i
    print(fact)  
