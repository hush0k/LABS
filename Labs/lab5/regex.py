import re

#1 task
def ab(list_word):
    for word in list_word:
        valid = re.compile(r'ab*', re.IGNORECASE)
        check = valid.findall(word)
        if check:
            print(word.strip(),"-->", end=" ", sep="")
            print(check)

#2 task
def ab2(list_word):
    for word in list_word:
        valid = re.compile(r'ab{2,3}', re.IGNORECASE)
        check = valid.findall(word)
        if check:
            print(word.strip(),"-->", end=" ", sep="")
            print(check)

#3 task
def underscore(list_word):
    for word in list_word:
        valid = re.compile(r'[a-z]+_+[a-z]+')
        check = valid.findall(word)
        if check:
            print(word.strip(),"-->", end=" ", sep="")
            print(check)

#4 task
def uppercase(list_word):
    for word in list_word:
        valid = re.compile(r'[A-Z][a-z]+')
        check = valid.findall(word)
        if check:
            print(word.strip(),"-->", end=" ", sep="")
            print(check)

#5 task
def any(list_word):
    for word in list_word:
        valid = re.compile(r'a[\W|\w]*b')
        check = valid.findall(word)
        if check:
            print(word.strip(),"-->", end=" ", sep="")
            print(check)

#6 task
def tocolumn(list_word):
    for word in list_word:
        find = re.compile(r'[ |,|.]')
        result = re.sub(find, ':', word)
        print(word.strip(),"-->", end=" ", sep="")
        print(result)

#7 task
def snaketocamel(list_word):
    for word in list_word:
        snake = re.compile(r'snake')
        valid = snake.findall(word)
        if valid:
            change = re.sub(snake, 'camel', word)
            print(word.strip(),"-->", end=" ", sep="")
            print(change)

#8 task
def splituppre(list_word):
    for word in list_word:
        check = re.findall(r'[A-Z][^A-Z]*', word)
        print(word.strip(),"-->", end=" ", sep="")
        print(check)

#9 task
def insert_space(list_word):
    for word in list_word:
        find = r'(?<=[a-z])(?=[A-Z])'
        change = re.sub(find,' ', word)
        print(word.strip(),"-->", change)

#Last task
def camel_to_snake(list_word):
    for word in list_word:
        snake = re.compile(r'camel')
        valid = snake.findall(word)
        if valid:
            change = re.sub(snake, 'snake', word)
            print(word.strip(),"-->", end=" ", sep="")
            print(change)



with open("checker.txt", "r") as file:
    list_word = file.readlines()

print("First task")
ab(list_word)

print("Second task")
ab2(list_word)

print("Third task")
underscore(list_word)

print("Fourth task")
uppercase(list_word)

print("Fifth task")
any(list_word)

print("Sixth task")
tocolumn(list_word)

print("Seventh task")
snaketocamel(list_word)

print("Eighth task")
splituppre(list_word)

print("Ninth task")
insert_space(list_word)

print("Last task")
camel_to_snake(list_word)