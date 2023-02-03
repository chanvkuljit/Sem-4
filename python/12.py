'''
12.Write a program to input a number and display whether number is prime or not.
'''

num=int(input("Enter Number:"))
ch=-0

if(num==1):
    print("Not Prime Number")
    
else:
    for i in range(1,num):
        if(num%i==0):
            ch=1
            
        else:
            ch=2

if(ch==1):
    print("Number is Prime",+num)
else:
    print("Number is Not Prime",+num)
