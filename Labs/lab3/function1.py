import random
#*1 task
def convert_grams_to_ounces(grams):
    print(grams / 28.3495231)
def convert_ounces_to_grams(ounces):
    print(ounces * 28.3495231)

choose = str(input("Choose the unit of measurement: \n 1)gram to ounce \n 2)ounce to gram"))
if choose == "gram to ounce":  
    grams = int(input())
    convert_grams_to_ounces(grams)
elif choose == "ounce to gram":  
    ounces = int(input())
    convert_ounces_to_grams(ounces)

#*2 task
def convert_farenheit_to_celsius(farenheit):
    print((farenheit - 32) * 5 / 9)

farenheit = int(input())
convert_farenheit_to_celsius(farenheit)


#*3 task
def solve(numheads, numlegs):
    rabbits = (numlegs - 2*numheads)/2
    chickens = numheads - rabbits
    print("Number of chickens: ", int(chickens))
    print("Number of rabbits: ", int(rabbits))
    
numheads = int(input())
numlegs = int(input())
solve(numheads, numlegs)

#*4 task
def filter_prime(list_num):
    prime_list = list_num.copy()
    for i in range(len(list_num)):
        if list_num[i] <= 2:
            continue
        else:
            for j in range(2,list_num[i]):
                if list_num[i] % j == 0:
                    prime_list.remove(list_num[i])
                    break  
    print(prime_list)
    
list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
filter_prime(list_num)

#*5 task
def permutation(strings):
    result = 1
    length = len(strings)
    for i in range(1, length + 1):
        result *= i
    print(result)

strings = input()
permutation(strings)


#*6 task
def reverse_words(strings):
    words = strings.split()
    words.reverse()
    print(" ".join(words))
    
strings = str(input())
reverse_words(strings)

#*7 task
def has_33(list ):
    ok = False
    for i in range(len(list) - 1):
        if list[i] == 3 and list[i + 1] == 3:
            ok = True
            break
    print(ok)
    
has_33([3, 1, 3])
has_33([1, 3, 3])
has_33([1, 3, 1, 3, 3])


#*8 task
def spy_game(list):
    index = 1
    zzs = False
    for i in range(len(list)):
        if index == 1 and list[i] == 0:
            index += 1
        elif index == 2 and list[i] == 0:
            index += 1
        elif index == 2 and list[i] == 7:
            index = 1
        elif index == 3 and list[i] == 0:
            index = 1
        elif index == 3 and list[i] == 7:
            zzs = True
            break
    print(zzs)

spy_game([1,2,4,0,0,7,5]) 
spy_game([1,0,2,4,0,5,7]) 
spy_game([1,7,2,0,4,5,0])

#*9 task
def radius_of_shere(radius):
    print(3.141592653589793 * radius**3*(4/3))

radius = int(input())
radius_of_shere(radius)

#*10 task
def unique_list(list):
    new_list = []
    for i in range(len(list)):
        if list[i] not in new_list:
            new_list.append(list[i])
    print(new_list)

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
unique_list(list)

#*11 task
def is_pollindrome(string):
    for i in range(len(string) // 2):
        if string[i]!= string[len(string) - i - 1]:
            return False
    return True

string = str(input())
if is_pollindrome(string):
    print("It is a pollindrome")
else:
    print("It is not a pollindrome")
    
#*12 task
def histogram(list):
    for i in range(len(list)):
        for j in range(list[i]):
            print("*", end="")
        print()

list = [4, 9, 3, 6]
histogram(list)


#*13 task
def guess_number():
    number = random.randint(1, 20)
    name = str(input("Hello! What is your name? "))
    print(f"Hello {name}, I am thinking of a number between 1 and 20")
    guess = int(input("Take a guess: "))
    cnt = 1
    while guess!= number:
        if guess > number and guess - number <= 3:
            print("Your guess is big.")
            cnt += 1
        elif guess > number and guess - number > 3:
            print("Your guess is too big.")
            cnt += 1
        elif guess < number and number - guess <= 3:
            print("Your guess is low.")
            cnt += 1
        elif guess < number and number - guess > 3:
            print("Your guess is too low.")
            cnt += 1
        guess = int(input("Take a guess: "))
        
    
    print(f"Good job, {name}! You guessed my number in {cnt} guesses!")
    
guess_number()
    
    

    



            
 