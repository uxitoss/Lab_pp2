#Task 1
N = int(input("Enter a number N: "))
def square_generator():
    for i in range(1, N + 1):
        yield i ** 2 

squares = square_generator()

print("Squares up to N:")
for square in squares:
    print(square)

#Task 2
n = int(input("Enter number: "))
def generate_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

print(",".join(map(str, generate_numbers(n))))

#Task 3
n = int(input("Enter the range: "))
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

for num in divisible_by_3_and_4(n):
    print(num)


#Task 4
a, b = 1, 5  
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

for square in squares(a, b):
    print(square)

def countdown(n):
    while n >= 0:
        yield n
        n -= 1

#Task 5
n = int(input("Enter the starting number: "))
for num in countdown(n):
    print(num)
