import math 

#1 task
degree = int(input("Enter a degree: "))
radian = math.radians(degree)
print(round(radian, 6)) #will rooud to 6 decimal places

#2 task
def trapizode(height, fist, second):
    area = height * (fist + second) / 2
    print(area)
    
height = 5
first = 5
second = 6
trapizode(height, first, second)


#3 task
def polygon_area(sides, length):
    area = (sides * pow(length, 2))/(4*math.tan(math.pi/sides))
    print(round(area))
    
sides = 4
length = 25
polygon_area(sides, length)

#4 task
def parallelogram_area(base, height):
    area = base * height
    print(float(area))

base = 5
height = 6
parallelogram_area(base, height)