#Task 1
def converting (sold_ounces, grams):
    sold_ounces = grams * 28.3495231
    return sold_ounces

#Task 2
def converting (F, C):
    C = (5 / 9)*(F – 32)
    return C

#Task 3
def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if 2 * chickens + 4 * rabbits == numlegs:
            return chickens, rabbits
        else:
            return "No solution" 

#Task 4
list = input([])
def prime(list):
    for i in range(len(list)):
        if 0 <= list[i] < 10:
            print(list[i])
    return list

#Task 5
string = input()
def permutation(string, prefix=""):
    for i in range(len(string)):
                remaining = string[:i] + string[i+1:]
                permutation(remaining, prefix + string[i])

#Task 6
def reverse(string):
    return " ".join(string.split()[::-1])

#Task 7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

#Task 8
def spy_game(nums):
    code = [0, 0, 7]
    for num in nums:
        if num == code[0]:
            code.pop(0)
        if not code:  
            return True
    return False


#Task 9
import math

def sphere_volume(radius):
    if radius < 0:
        return "Incorrect value"
    volume = (4 / 3) * math.pi * radius**3
    return volume

#Task 10
def get_unique_elements(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

#Task 11
def is_palindrome(text):
    cleaned_text = ""
    for char in text:
        if char.isalnum():
            cleaned_text += char.lower()
    return cleaned_text == cleaned_text[::-1]

#Task 12
def histogram(numbers):
    for num in numbers:
        print('*' * num)

#Task 13
import random

def guess_the_number():
    print("Hello! What is your name?")
    name = input()
    
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    secret_number = random.randint(1, 20)
    guesses = 0
    
    while True:
        print("Take a guess.")
        guess = int(input())
        guesses += 1
        
        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
            break









