#In this program, I write python program to check if a string is a palindrome

#Function Definition
def palindrome(str):
    #str is the actual string and str[::-1] is the string in reverse
    #We check if they are equal, it returns True and if not, returns False
    return str == str[::-1]
 
 
#Amma is a palindrome
amma = "amma"

#Python is not a palindrome
python = "python"

#check_amma holds the bool value of amma being a palindrome or not
check_amma = palindrome(amma)

#check_python holds the bool value of python being a palindrome or not
check_python = palindrome(python)
 
#checking the bool value of check_amma and printing the Output based on that
if check_amma:
    print(True)
else:
    print(False)

#checking the bool value of check_python and printing the Output based on that
if check_python:
  print(True)
else:
  print(False)
