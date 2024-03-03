import os
#!1 task 
def name_files():
    path = str(input("Enter the path: "))
    print("\033[1mDirectories in the path:\033[0m\n")
    for dir in os.listdir(path):
        if os.path.isdir(os.path.join(path, dir)):
            print(dir)
            
    print("\n\033[1mFiles in the path:\033[0m\n")
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            print(file)
    print("\n\033[1mAll of them:\033[0m\n")
    for all in os.listdir(path):
        print(all)


#!2 task
def access():
    path = str(input('Enter the path: '))
    if os.path.exists(path):
        print('The path exists✔️')
        is_readable = os.access(path, os.R_OK)
        if is_readable:
            print('The file is readable✔️')
        else:
            print('The file is not readable❌')
        is_writable = os.access(path, os.W_OK)
        if is_writable:
            print('The file is writable✔️')
        else:
            print('The file is not writable❌')
        is_executable = os.access(path, os.X_OK)
        if is_executable:
            print('The file is executable✔️')
        else:
            print('The file is not executable❌')
    else:
        print('The path does not exist❌')

#!3 task
def exsits():
    path = str(input('Enter the path: '))
    if os.path.exists(path):
        print('The path exists✔️')
        path_name = os.path.basename(path)
        path_dir = os.path.dirname(path)
        print('File name is: ', path_name)
        print('File path is: ', path_dir)
        
#!4 task
def number_of_lines():
    path = input("Enter the path: ")
    count = 0
    with open(path, 'r') as file:
        list_word = file.readlines()
        for line in list_word:
            count += 1
        print(count)
        

#!5 task
def write_list():
    path = str(input("Enter the path: "))
    with open(path, 'a') as file:
        listis = ['Mama', 'Papa', 'Sister', 'Bratha', 'Gara']
        file.write('\n'.join(listis))
        

import string
#!6 task
def create_file():
    stringalphabet = string.ascii_lowercase

    for letter in stringalphabet:
        filename = letter + '.txt'
        with open(filename, 'w') as file:
            file.write(letter)
            
#!7 task
def copy_to_other():
    path = str(input("Enter the path: "))
    new_path = str(input("Enter the new path: "))
    with open(path, 'rb') as file:
        abstract = file.read()
    with open(new_path, 'ab') as new_file:
        new_file.write(abstract)
        

#!8 task
def delete_existing_file():
    path = str(input("Enter the path: "))
    if os.path.exists(path):
        os.remove(path)
        print('The file was exists and have been deleted✔️')
    else:
        print('The file does not exist❌')

        









task = int(input("Enter the task number: "))
if task == 1:
    name_files()
elif task == 2:
    access()
elif task == 3:
    exsits()
elif task == 4:
    number_of_lines()
elif task == 5:
    write_list()
elif task == 6:
    create_file()
elif task == 7:
    copy_to_other()
elif task == 8:
    delete_existing_file()
    
    
