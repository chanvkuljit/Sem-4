'''
7.Write a program to input age of person and display message as 
follows 
- If age < 12 print You are Kid 
- If age between 12 to 17 print You are teenager 
- If age between 18 to 60 print you are Adult 
If age > 60 print You are Senior Citizen 
'''

age=int(input("Enter Your Age:"))

if(age<12):
    print("You are Kid")
    
elif((age<=12) and (age>=17)):
    print("Your are Teenager")
    
elif((age<=18) and (age>=60)):
    print("Your are Adult")
    
elif(age>60 and age<150):
    print("Your are Senior Citizen")

else:
    print("Invalid Age")

