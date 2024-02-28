#1 task
def square_nums(N):
    for i in range(1, N+1):
        yield i**2
        
n = int(input("Enter a number: "))
squere = square_nums(n)
print(*squere )

#2 task
def even_numbers(N):
    for i in range(1, N+1):
        if i % 2 == 0:
            yield i

n = int(input("Enter a number: "))
even = even_numbers(n)
print(*even, sep = ", ")

#3 task
def div_three_and_four(N):
    for i in range(1, N+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
            
n = int(input("Enter a number: "))
divisiable_nums = div_three_and_four(n)
print(*divisiable_nums, sep = ", ")

#4 task
def sq_a_b(N, M):
    for i in range(N, M+1):
        yield i**2

n = int(input("Enter a number: "))
m = int(input("Enter a number: "))
sq_ab = sq_a_b(n, m)
print(*sq_ab, sep = ", ")

#5 task
def rev_lsit(N):
    for i in range(N, 0, -1):
        yield i

n = int(input("Enter a number: "))
rev_list = rev_lsit(n)
print(*rev_list, sep = ", ")