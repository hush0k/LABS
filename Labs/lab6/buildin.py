import math
import time

#!1 task
def multy(list):
    return math.prod(list)

#!2 task
def sum_u_l():
    text = str(input("Enter the text: "))
    lower = sum(1 for letter in text if letter.islower())
    upper = sum(1 for letter in text if letter.isupper())
    
    print('Number of lower case letters: ', lower)
    print('Number of upper case letters: ', upper)

#!3 task
def is_palindrome():
    text = str(input("Enter the text: "))
    if text == text[::-1]:
        print(text, "is a palindrome")
    else:
        print(text, "is not a palindrome")
    
#!4 task
def root():
    number = int(input("Enter the number: "))
    miliseconds = int(input("Enter the number of miliseconds: "))
    seconds = miliseconds/1000
    
    time.sleep(seconds)
    result = int(math.sqrt(number))
    
    print(f'The root of {number} is: {result} after {miliseconds} miliseconds')

def true_all(tuple):
    false = sum(1 for i in tuple if i == False)
    if false > 0:
        return False
    else:
        return True
    




task = int(input("Enter the task number: "))
if task == 1:
    n = int(input("Enter the number of elements: "))
    list = []
    for i in range(n):
        list.append(int(input()))
    print(multy(list))
elif task == 2:
    sum_u_l()
elif task == 3:
    is_palindrome()
elif task == 4:
    root()
elif task == 5:
    tup = (True, True, True, True, True, True, True, False, True)
    print(true_all(tup))
    