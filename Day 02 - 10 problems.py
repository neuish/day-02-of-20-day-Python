#1. Write a program that checks if a number is positive, negative, or zero.
def number_checker():
    number = int(input('enter a positive or a negative number or a zero:'))

    if number == 0: 
        print(f'{number} is a 0')

    elif number > 0 :
        print(f'{number} is a positive number')

    elif number < 0 :
        print(f'{number} is a negative number')

#2. Create a program that checks whether a year is a leap year.

def leap_year():
    year = int(input('enter a year to check its leap year:'))

    if (year % 4 == 0) and (year % 100 != 0 or year % 400 ==0):
        print(f'{year} is a leap year')
    else:
        print(f'{year}is not a leap year')

#3. Write a program that asks the user for their age and prints whether they can vote.

def vote_rights():
    age = int(input('enter your age:'))

    if age >= 18 :
        print('you can vote')
    else:
        print('you dont yet have the voting rights')

#4. Write a program that grades a student based on their marks.
def grade():
    grade = float(input('enter your grade:'))

    if grade < 35 : print('fail')
    elif grade < 50 : print('3rd division')
    elif grade < 60 : print('second division')
    elif grade < 80 : print('first Division')
    else: print('distinction')

#5. Modify the discount calculator to implement tiered pricing. For example, if the price is below $50, apply a 5% discount, if between $50 and $100, apply a 10% discount, and if above $100, apply a 20% discount.
def discount_Calc():
    price = float(input('enter the price:'))

    if price < 50: 
        discount = price * 0.05
        print(f'the discounted price is {discount}')
        
    elif 50 <= price <= 100:
        discount = price * 0.10
        print(f'the discounted price is {discount}')
    
    elif price > 100: 
        discount = price * 0.30
        print(f'the discounted price is {discount}')

#6. Create a program that simulates a login system by asking the user for a username and password. Print "Access granted" if the username and password match predefined values; otherwise, print "Access denied."
def login_system():
    defined_username = 'username'
    defined_password = 'pass1234@@'

    username = input ('enter the username:')
    password = input ('enter the password:')

    if username == defined_username and password == defined_password: print('access granted')
    else: print('invalid username and password')

#7. Write a program that calculates the income tax based on a progressive tax system. Define tax brackets (e.g., 10% for income up to $50,000, 20% for income between $50,001 and $100,000, and 30% for income above $100,000) and compute the tax for any given income.
def income_tax():
    income = float(input('enter your income'))

    if income <= 50000:
        tax = income * 0.10
        print(f'the tax for the given {income} is {tax}')
       
    if 50001 <= income <= 100000:
        tax = income * 0.20
        print(f'the tax for the given {income} is {tax}')

    if income > 100000:
        tax = income * 0.30
        print(f'the tax for the given {income} is {tax}')

#8. Write a program that solves a quadratic equation (ax² + bx + c = 0) using the quadratic formula. Handle cases where the discriminant is negative, zero, or positive and print the appropriate solution(s).
import math
import cmath
def quadratic_eq():
    a, b, c = map(int, input('enter the value for a, b, and c saperated by a space').split())
    D = pow(b, 2) - (4*a*c)

    if D > 0:
    # Two real roots
        root1 = (-b + math.sqrt(D)) / (2 * a)
        root2 = (-b - math.sqrt(D)) / (2 * a)
        print(f"The equation has two real roots: {root1} and {root2}")
    
    elif D == 0:
    # One real root
        root = -b / (2 * a)
        print(f"The equation has one real root: {root}")
    
    else:
    # Two complex roots
        root1 = (-b + cmath.sqrt(D)) / (2 * a)
        root2 = (-b - cmath.sqrt(D)) / (2 * a)
        print(f"The equation has two complex roots: {root1} and {root2}")

def main_menu():
    while True:
        print('\n .... Main Menu ....')
        print('1. Number Checker')
        print('2. Leap Year Checker')
        print('3. voting rights')
        print('4. Grade Checker')
        print('5. discount calculator')
        print('6. login system')
        print('7. income tax')
        print('8. quadratic equation')
        print('0. Exit')

        choice = input('enter your choice from the given options')

        if choice == '1':
            number_checker()

        elif choice == '2':
            leap_year()
        
        elif choice == '3':
            vote_rights()
        
        elif choice == '4':
            grade()

        elif choice == '5':
            discount_Calc()
        
        elif choice == '6':
            login_system()
        
        elif choice == '7':
            income_tax()

        elif choice == '8':
            quadratic_eq()

        elif choice == "0":
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid choice, please try again.")

# Running the main menu
main_menu()