#APP.
import pathlib as path
class APP:  
    def even_or_odd():
        number = int(input("Enter number to see if it is even or odd: "))

        if number % 2 == 0:
            print("The number is even")
            return
        else:
            print("The number is odd.")
    def sum_off_numbers():
        n = int(input("Enter number: "))
        a = 0

        for i in range(1, n+1):
            a += n
        print(f"The sum of number is {a}")
    def finding_list():
        example = [4, -2, 7, -1, 0, 8]

        for e in range(len(example)):
            if example[e] > 0:
                print(f" The number of negatives are {example[e] > 0}")
                return
    def print_largest_number_in_list():
        try:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            num3 = int(input("Enter third number: "))
            num4 = int(input("Enter fourth number: "))
            num5 = int(input("Enter fifth number: "))
        except ValueError:
            print("Cannot add numbers.")
            return None
        
        numbers = [num1, num2, num3, num4, num5]

        sorting = sorted(numbers, reverse=True)
        print(sorting)
    def sorting_list():
        example = [1,2,3,4,5]

        sorting_reverse = example.sort(reverse=True)
        print(sorting_reverse)

    def vowel():
        word = input("Enter string: ")
        vowel_count = 0

        vowels = ["a", "e", "i", "o", "u"]

        for w in word.lower():
            if w in vowels:
                vowel_count += 1
            
        print(f"Number of vowels is {vowel_count}, and vowels in ur word are {w}")

    def multiply():
        raw = input("Enter number: ")
        if not raw.isdigit():
            print("Enter number.")
            return
        n = int(raw)
        
        for i in range(n, 11):
            n*=i
        print(i)
    
    def new_list():
        example = [1,2,2,3,4,4,5]
        new_list = []

        for e in range(len(example)):
            if example[e] not in new_list:
                new_list.append(example[e])
        print(example)

    def marks():
        try:
            sub1 = int(input("Enter first subject"))
            sub2 = int(input("Enter second subject"))
            sub3  = int(input("Enter first subject"))
        except ValueError:
            print("Cannot use numbers.")
            return None
        
        sum  = sub1 + sub2 + sub3

        if sum >= 90:
            print("Grade A")
            return
        if sum > 75 and sum < 90:
            print("Grade B")
            return
        if sum > 50 and sum < 74:
            print("Grade C.")
            return
        if sum < 50:
            print("Fail.")
            return
    
    def finding_second_largest():
        example = [2,1,21,31]

        new = list(set(example))

        new.sort()

        if len(new) >= 2:
            print(f"Second largest number is {new[-2]}")
    
    def duplicate():
        example = [1,2,2,3,3,3,4]
        new = list(set(example))

        for n in new:
            count = example.count(n)
            if count > 1:
                print(f"Found {count} duplicates in {example} ")
            
    def chatbot():
        a = input("Enter word('hello', 'bye'): ")

        if a.lower() == "Hello":
            print("Hello, how are you.")
            return
        if a.lower() == "Bye":
            print("Goodbye")
            return
        else:
            print("I dont understand.")
    def scores():
        example = [45,78,88, 92, 67, 55, 100]

        print(f"Highest is {max(example)}, Lowest is {min(example)}, and average is {sum(example)/ len(example)}")
    
    def spam():
        word = input("Enter a setence(trust me.): ")

        banned_words = ["win","free", "money" ]

        if word.lower() in banned_words:
            print("This is a spam.")
        else:
            print("Safe message")

    def palindrome():
        word = input("Enter word: ")

        if word == word[::-1]:
            print("It is a palindrome")
            return
    def password_teller():
        password = input("Enter your password: ")

        length = 8
        has_digits = False
        has_uppercase = False

        for p in password:
            if p.isdigit():
                has_digits = True
            if p.isupper():
                has_uppercase = True
        
        if len(password) >= length and has_digits and has_uppercase:
            print("Strong password.")
        else:
            print("Weak password")
            print(f"Your password should have {length}")
            print("Your Password should contain digits.")
            print("Your password should contain Uppercase letters.")
        
    def greater_than_30():
        example = [23,12,45,67,34,89,2]
        new_list = []

        for e in example:
            if example[e] > 30:
                new_list.append(e)
        print(new_list)

def main():
    while True:
        print("\n" + "="*30)
        print("\nPractice(The overkill kind.)\n")
        print("="*30)
        print("1-4: Math & Grades")
        print("5-11: List & Number Tools")
        print("12-17: String & Security")
        print("0: Exit")
        
        try:
            choice = int(input("\nSelect an option (0-17): "))
            
            if choice == 0: break
            elif choice == 1: APP.even_or_odd()
            elif choice == 2: APP.sum_off_numbers()
            elif choice == 3: APP.multiply()
            elif choice == 4: APP.marks()
            elif choice == 5: APP.finding_list()
            elif choice == 6: APP.print_largest_number_in_list()
            elif choice == 7: APP.sorting_list()
            elif choice == 8: APP.finding_second_largest()
            elif choice == 9: APP.duplicate()
            elif choice == 10: APP.new_list()
            elif choice == 11: APP.greater_than_30()
            elif choice == 12: APP.vowel()
            elif choice == 13: APP.chatbot()
            elif choice == 14: APP.spam()
            elif choice == 15: APP.palindrome()
            elif choice == 16: APP.password_teller()
            elif choice == 17: APP.scores()
            else: print("Invalid number.")
        except ValueError:
            print("Enter a number.")

main()
    




            









        

        
        
            

        
     
            
        
   





