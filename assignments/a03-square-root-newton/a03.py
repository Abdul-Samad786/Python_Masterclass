## IMPORTS GO HERE
from math import sqrt
## END OF IMPORTS

epsilon = 1e-4

#### YOUR CODE FOR sqrt() FUNCTION GOES HERE ####
def sqrt(number, guess=1):
    if good_enough(number, guess):
        return guess
    else:
        improved_guess = improve_guess(guess,number)
        return sqrt(number, improved_guess)
#### End OF MARKER


#### YOUR CODE FOR average() FUNCTION GOES HERE ####
def average(first_number, second_number):
    avg = (first_number + second_number) / 2
    return avg
#### End OF MARKER


#### YOUR CODE FOR improve_guess() FUNCTION GOES HERE ####
def improve_guess(guess,number):
    new_guess = average(guess, number / guess)
    return new_guess
#### End OF MARKER


# Function of good enough
def good_enough(sqrt_number, guess):
    if abs(guess * guess - sqrt_number) < epsilon:
        return True
    else:
        return False


if __name__ == '__main__':
    print(sqrt(36, 5))