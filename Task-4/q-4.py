#Question-4
num=int(input("Enter a number: "))
num1=str(num)
if num1 == num1[::-1]:
    print("it is a palindrome!") 

else:
    print("it is not a palindrome!")
