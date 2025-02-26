#Task 1
import math

degrees = float(input("Enter angle in degrees: "))

def degrees_to_radians():
    radians = degrees * (math.pi / 180)
    print(degrees, "Degrees is equal to ", radians, "radians")

degrees_to_radians()


#Task 2
height = float(input("Enter the height: " ))
first_value = float(input("Enter the first value: " ))
second_value = float(input("Enter the second value: " ))

def area_of_trap():
    formula = ((first_value + second_value) * height)/2
    print("The area of trapeziod is: ", formula)

area_of_trap()


#Task 3
import math

def polygon_area():
    n = int(input("Input number of sides: "))
    s = float(input("Input the length of a side: "))
    area = (n * s**2) / (4 * math.tan(math.pi / n))
    print("The area of the polygon is: ", area) 

polygon_area()


#Task 4
base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))

def parallelogram_area():
    area = base * height
    print("Expected Output: ", area)

parallelogram_area()

