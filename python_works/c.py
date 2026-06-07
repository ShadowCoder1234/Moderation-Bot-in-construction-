from time import sleep as s
import sys

def menu():
    print("\nWelcome to my pratical Tests, here u can find the following tests.\n")
    print("1. Find the area of a circle.")
    print("2. Find the net salary.")
    print("3. Find if a number is even or odd.")
    print("4. Find if a number is a buzzword(divisble by 10 or 7).")
    print("5. Find Greater number between 2 numbers.")
    print("6. Find Greater number between three numbers.")
    print("7. Arrange in ascending order or descending order.")
    print("8. Loops(while and for loops.)")
    print("9. Learn lists and its function.")
    print("Exit")

def FindAreaOfCircle():
    try:
        radius = int(input("What is the radius?: "))
        result = 3.14 * radius ** 2
        s(1)
        print(f"Result is {result}")
    except ValueError:
        print(f"Cannot add numbers")
        return

def FindNetSalary():
    try:
        basic_salary = int(input("What is ur basic salary?: "))
    except ValueError:
        print("Cannot add words.")
        return
    s(0.5)
    hra = 33 / 100 * basic_salary
    da = 27 / 100 * basic_salary
    pf = 24 / 100 * basic_salary
    net_salary = basic_salary + hra + da - pf
    print("Finding net salary...")
    s(1.2)
    print(net_salary)

def FindNumberEvenOrOdd():
    try:
        check_no = int(input("Enter number: "))
    except ValueError:
        print("Cannot add words.")
        return

    print("Checking number is even or odd...")
    s(1.2)
    if check_no % 2 == 0:
        print("Number is even.")
    else:
        print("Number is odd")

def Buzzword():
    try:
        number = int(input("Enter number: "))
    except ValueError:
        print("Cannot add numbers.")
        return
    print("Checking number is buzzword or not...")
    s(1.2)
    if number % 10 == 0 or number % 7 == 0:
        print("Number is buzzword.")
    else:
        print("Number is not a buzzword.")

def GreaterNo():
    try:
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter second number: "))
    except ValueError:
        print("Cannot add words.")
        return
    print("Finding number that is greater...")
    s(1.2)

    if num1 > num2:
        print(f"{num1} is greater than {num2}")
    elif num2 > num1:
        print(f"{num2} is greater than {num1}")
    else:
        print("Both numbers are equal")

def GreaterNoThree():
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        num3 = int(input("Enter third number: "))
    except ValueError:
        print("Cannot add words.")
        return
    print("Calcuting which numbers are greater.")
    s(1.2)

    if num1 > num2 and num1 > num3:
        print(f"{num1} is greater than both {num2} and {num3}")
    elif num2 > num1 and num2 > num3:
        print(f"{num2} is greater than both {num1} and {num3}")
    elif num3 > num1 and num3 > num2:
        print(f"{num3} is greater than bot {num1} and {num2}")
    else:
        print("All numbers are equal or two numbers are equal")

def arrangeOrder():
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        num3 = int(input("Enter third number: "))
    except ValueError:
        print("Cannot put words.")
        return
    print("Arranging values in ascending order...")
    s(1.2)

    if num1 < num2 and num1 < num3:
        if num2 < num3:
            print(f"{num1}, {num2}, {num3}")
        else:
            print(f"{num1}, {num3}, {num2}")
    elif num2 < num1 and num2 < num3:
        if num1 < num3:
            print(f"{num2}, {num1}, {num3}")
        else:
            print(f"{num2}, {num3}, {num1}")
    elif num3 < num1 and num3 < num2:
        if num1 < num2:
            print(f"{num3}, {num1}, {num2}")
        else:
            print(f"{num3}, {num2}, {num1}")

    choice = input("Do u want to put the same numbers in descending order?(y,n): ").lower()

    if choice == "y":
        print("Arranging numbers in descending order...")
        s(1.2)

        if num1 > num2 and num1 > num3:
            if num2 > num3:
                print(f"{num1}, {num2}, {num3}")
            else:
                print(f"{num1}, {num3}, {num2}")
        elif num2 > num1 and num2 > num3:
            if num1 > num3:
                print(f"{num2}, {num1}, {num3}")
            else:
                print(f"{num2}, {num3}, {num1}")
        elif num3 > num1 and num3 > num2:
            if num1 > num2:
                print(f"{num3}, {num1}, {num2}")
            else:
                print(f"{num3}, {num2}, {num1}")
    elif choice == "n":
        return

def loops():
    print("HELLO AND WELCOME TO LOOPS.")
    s(2)
    try:
        n = int(input("Enter value."))
    except ValueError:
        print("Cannot put words")
        return

    # With for loops
    for i in range(1, n + 1):
        print(i)
        s(0.3)

    sum_choice = input("Do u want to see the sum of this using both for loops and while loop?(y,n): ")

    if sum_choice == "y":
        s_k = 0
        for i in range(1, n + 1):
            s_k += i
        print("With for loops:", s_k)

        s_k = 0
        a = 1
        while a <= n:
            s_k += a
            a += 1
        print("With while loops:", s_k)

def lists():
    print("Welcome to Lists")
    example = [1, 2, 3, 4]
    s(0.5)
    print("Lists has append function which is used to add a value.")
    example.append(5)
    print(example)
    s(0.5)
    print("Now we have extend, which is used to extend the list.")
    example.extend([5, 6])
    print(example)
    s(0.5)
    print("Now we have remove in lists, which is used to remove a value from the list.")
    example.remove(5)
    print(example)
    s(0.5)
    print("And lastly(for this syllabus is) the sort function, which is used to sort the values")
    example.sort()
    print(example)
    s(0.2)
    print("We can also use to reverse the sort.")
    example.sort(reverse=True)
    print(example)

def handler():
    while True:
        menu()
        choice = input("Choose(1./2./3./4./5./6./7./8./9.) \n Or choose exit.: ")

        if choice == "1":
            FindAreaOfCircle()
        elif choice == "2":
            FindNetSalary()
        elif choice == "3":
            FindNumberEvenOrOdd()
        elif choice == "4":
            Buzzword()
        elif choice == "5":
            GreaterNo()
        elif choice == "6":
            GreaterNoThree()
        elif choice == "7":
            arrangeOrder()
        elif choice == "8":
            loops()
        elif choice == "9":
            lists()
        elif choice.lower() == "exit":
            break
        else:
            print("Function is incorrect or not availble.")

handler()



