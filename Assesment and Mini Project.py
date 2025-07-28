# Q1. Write a program to check if a given number is Positive, Negative or Zero.
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


#Q2. Write a program to check if a given number is odd or even.
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

#Q3. Given two non-negative values, print true if they have the same last digit, such as with 27 and 57
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a >= 0 and b >= 0:
    if a % 10 == b % 10:
        print("True")
    else:
        print("False")
else:
    print("Please enter non-negative numbers.")


#Q4. Write a program to print numbers from 1 to 10 in a single row with one tab space.
for i in range(1, 11):
    print(i, end="\t")

#Q5. Write a program to print even numbers between 23 and 57. Each number should be printed in a seperate row.
for i in range(23, 58):
    if i % 2 == 0:
        print(i)

#Q6. Write a program to check if a given number is prime or not.
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")


#Q7. Write a program to print prime numbers between 10 and 99.
for num in range(10, 100):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num)


#Q8. Write a program to print the sum of all the digits of a given number.
num = int(input("Enter a number: "))
sum_digits = 0
while num > 0:
    sum_digits += num % 10
    num = num // 10
print("Sum of digits:", sum_digits)


#Q9. Write a program to reverse a given number and print.
num = int(input("Enter a number: "))
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
print("Reversed number:", reverse)


#Q10. Write a program to find if the given number is palindrom or not.
num = int(input("Enter a number: "))
original = num
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")


# MINI PROJECT 
# Tech Module: Python Fundamentals
# 1.	create a python program that asks the user how far they want to travel. 
# if they want to travel less than three miles tell them to ride Bicycle. 
# if they want to travel more than three miles, but less than three hundred miles, tell them to ride Motor-cycle. 
# if they want to travel three hundred miles or more tell them to driver Super-Car.
# Sample Output:
# How far would you like to travel in miles? 2500
# I suggest Super-Car to your destination
# Travel mode suggestion based on distance
def suggest_travel_mode():
    distance = float(input("How far would you like to travel in miles? "))

    if distance < 3:
        print("I suggest Bicycle to your destination")
    elif distance < 300:
        print("I suggest Motor-cycle to your destination")
    else:
        print("I suggest Super-Car to your destination")


suggest_travel_mode()




# 2.	Let's assume you are planning to use your python skills to build an App for Mobile.
# You decide to host your application on servers running in the cloud.
#  you pick a hosting provider that charges $0.51 per hour. 
# you will launch your services using one server and want to know how much it will cost to operate per day, per week, per month.
# Write a python program that displays the answers to the following questions:
# How much does it cost to operate one server per day?
# How much does it cost to operate one server per week?
# How much does it cost to operate one server per month?
# How much days can I operate one server with $918?



def server_costs():
    hourly_rate = 0.51
    hours_per_day = 24
    days_per_week = 7
    days_per_month = 30  

   
    cost_per_day = hourly_rate * hours_per_day
    cost_per_week = cost_per_day * days_per_week
    cost_per_month = cost_per_day * days_per_month

    print(f"Cost to operate one server per day: ${cost_per_day:.2f}")
    print(f"Cost to operate one server per week: ${cost_per_week:.2f}")
    print(f"Cost to operate one server per month: ${cost_per_month:.2f}")

   
    total_budget = 918
    days_with_budget = total_budget / cost_per_day
    print(f"With $918, you can operate the server for {days_with_budget:.2f} days.")


server_costs()

# Tech Module: DATA STRUCTURE
# 1. Create a dictionary that contains a list of people and one interesting fact about each of them.
# Display each person and his or her interesting fact to the screen. Next, change a fact about one of the people. 
# Also add an additional person and corresponding fact. Display the new list of people and facts. Run the program multiple times and notice if the order changes.
# Sample output:
# Jeff: Is afraid of Dogs.
# David: Plays the piano.
# Jason: Can fly an airplane.
# Jeff: Is afraid of heights.
# David: Plays the piano.
# Jason: Can fly an airplane.
# Jill: Can hula dance.

people_facts = {
    "Jeff": "Is afraid of Dogs.",
    "David": "Plays the piano.",
    "Jason": "Can fly an airplane."
}


print("Original facts:")
for name, fact in people_facts.items():
    print(f"{name}: {fact}")


people_facts["Jeff"] = "Is afraid of heights."


people_facts["Jill"] = "Can hula dance."


print("\nUpdated facts:")
for name, fact in people_facts.items():
    print(f"{name}: {fact}")


# 2. Given the participant's score sheet for your University Sports Day, you are required to find the runner-up score. 
# You have scores. Store them in a list and find the score of the runner-up.
# Sample input: [2, 3, 6, 6, 5]
# Sample output: 5
# Explanation: Given list is [2, 3, 6, 6, 5]. 
# The maximum score is 6, second maximum is 5. 
# Hence, we print 5 as the runner-up score.


def find_runner_up(scores):
    
    unique_scores = list(set(scores))
    unique_scores.sort(reverse=True)

    if len(unique_scores) < 2:
        return "No runner-up. Not enough unique scores."

    
    return unique_scores[1]

scores = [2, 3, 6, 6, 5]
print("Runner-up score:", find_runner_up(scores))


# 3. You have a record of n students. Each record contains the student's name, and their percent marks in Math, Physics and Chemistry. 
# The marks can be floating values. You are required to save the record in a dictionary data type.
# Student's name is the key. Marks stored in a list is the value. The user enters a student's name. 
# Output the average percentage marks obtained by that student.
# Formula: (sum of marks) / (no of subjects)
# Sample input: { "Krishna":
# [67, 68, 69],
# "Arjun": [70, 98, 63],
# "Malika": [52, 56, 60] }
# Sample output:
# Enter a name: Malika
# Average percentage mark: 56
# Explanation:
# Marks for Malika are [52, 56, 60] whose average is (52 +56 +60)/3 => 56

student_records = {
    "Krishna": [67, 68, 69],
    "Arjun": [70, 98, 63],
    "Malika": [52, 56, 60]
}


name = input("Enter a name: ")

if name in student_records:
    marks = student_records[name]
    average = sum(marks) / len(marks)
    print(f"Average percentage mark: {int(average)}")
else:
    print("Student not found.")


# 4. Given a string of n words, help Alex to find out how many times his name appears in the string.
# Constraint: 1 <= n <= 200
# Sample input: Hi Alex WelcomeAlex Bye Alex.
# Sample output: 3
# Explanation: Alex name appears 3 times in the string. Hi Alex WelcomeAlex
# Bye Alex.

def count_alex_occurrences(text):
    return text.count("Alex")

input_string = input("Enter the string: ")
count = count_alex_occurrences(input_string)
print("Number of times 'Alex' appears:", count)

# Tech Module: Functions/Modules/Packages
# 1. Write a Python function that accepts a hyphen-separated sequence of colors as input and 
# returns the colors in a hyphen-separated sequence after sorting them alphabetically.
# Constraint: All the colors will be completely in either lower case or upper case.
# Sample input 1: green-red-yellow-black-white
# Sample output 1: black-green-red-white-yellow
# Sample input 2: PINK-BLUE-TAN-PURPLE
# Sample output 2: BLUE-PINK-PURPLE-TAN

def sort_colors(color_sequence):
    colors = color_sequence.split("-")         
    colors.sort()                              
    return "-".join(colors)                    

# 2. Create a Python module with the following functions:
# Function Name
# ispalindrome(name): Given the user name as input, this function should tell us whether the name is a palindrome or not.
# count_the_vowels(name)
# Task: Given the user name as input, this function should tell us how many vowels are present in it.
# frequency_of_letters(name): Given the user name as input, this function should tell us how many times each letter appears in the name.
# Note: name will be completely in either lower case or upper case
# Import the module in another python script and test the functions by passing appropriate inputs.
# Sample input 1: bob
# Sample output 1:
# Yes it is a palindrome.
# No of vowels: 1
# Frequency of letters: b-2, 0-1

# string_utils.py

def ispalindrome(name):
    if name == name[::-1]:
        return "Yes it is a palindrome."
    else:
        return "No it is not a palindrome."

def count_the_vowels(name):
    vowels = 'aeiouAEIOU'
    count = sum(1 for char in name if char in vowels)
    return f"No of vowels: {count}"

def frequency_of_letters(name):
    freq = {}
    for char in name:
        freq[char] = freq.get(char, 0) + 1
    
    freq_str = ", ".join(f"{char}-{count}" for char, count in freq.items())
    return f"Frequency of letters: {freq_str}"

# test_module.py

import string_utils  
# Sample input
name = "bob"

# Testing functions
print(string_utils.ispalindrome(name))
print(string_utils.count_the_vowels(name))
print(string_utils.frequency_of_letters(name))

# Tech Module: Command Line Arguments
# 1. Through command line arguments three strings separated by space are given to you. 
# Each string is a series of numbers separated by hyphen(-). You like all the numbers in string 1 and dislike all the numbers in string 2.
# Third string contains the numbers given to you. Your initial happiness is 0.
# When you encounter a number which is present in string 1, add 1 to your happiness, if it is present in string 2, add -1 to your happiness. 
# Otherwise, your happiness does not change. Output your final happiness at the end.
# Sample input 1:
# 3-1
# 5-7
# -5-3-8
# Sample output 1: 1
# Explanation:
# Numbers in string 1:
# 3, 1
# Numbers in string 2:
# 5, 7
# Numbers given to you: 1, 5, 3, 8
# You gain 1 unit of happiness for numbers 1 and 3 which are in string 1. Your total happiness is 2 now.
# You lose 1 unit of happiness for number 5 which is in string 2. Your total happiness in 1 now.
# 8 is not present in either of the strings, so your happiness does not change.
# Final happiness is 1.

import sys

def calculate_happiness(likes_str, dislikes_str, input_str):
    # Convert hyphen-separated strings to sets/lists of integers
    likes = set(map(int, likes_str.split('-')))
    dislikes = set(map(int, dislikes_str.split('-')))
    given = list(map(int, input_str.split('-')))

    # Initialize happiness score
    happiness = 0

    for num in given:
        if num in likes:
            happiness += 1
        elif num in dislikes:
            happiness -= 1

    return happiness

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python happiness_score.py <likes> <dislikes> <given>")
        sys.exit(1)

    likes_str = sys.argv[1]
    dislikes_str = sys.argv[2]
    input_str = sys.argv[3]

    result = calculate_happiness(likes_str, dislikes_str, input_str)
    print(result)

# Tech Module: 10 Operations
''' 1. Your friend has sent you a text file containing n lines. He sent a secret message with it, which tells you the place and time where you have to go and meet him.
He challenges you to find it out without seeing the content of the file. He has given hints to find it. Let's surprise him by breaking the challenge with our python code.
Hints to find the secret message:
1. The number of lines in the file tells you the meeting time.
Note: 1<= number of lines <= 24
If the number of lines is exceeding 12, you need to convert it to 12 hour format. For example,
If the number of lines is 15, then the meeting time is 3 PM.
If the number of lines is 10, then the meeting time is 10 AM.
2. The word appearing for the maximum number of times tells you the meeting place.
Note: Meeting place will be a street name.
For example,
If the word Oxford appears for the maximum number of times, then meeting place is Oxford Street.
If the word Park appears for the maximum number of times, then meeting place is Park Street. 
Sample input 1:
Sample.txt
Cricket, a bat-and-ball park game played between two teams of eleven park players on a field at the park center of which is a 20-metre (22-yard) pitch with a wicket at each end, each park comprising two bails balanced on three stumps. The batting park scores runs by striking the ball bowled at the park wicket with the park bat, while the bowling and park fielding side tries to prevent this and dismiss each park player (so they are "out"). Means of park include being bowled, when the ball hits the park and dislodges the bails, and by the fielding side park the ball after it is hit by the bat, but before it hits the park. When ten park have been dismissed, the innings ends and the teams park roles.
Sample output 1:
Meeting time: 9 AM
Meeting place: Park Street
Explanation: Number of lines is 9. The word park appears for the maximum of 15 times.
'''
import string
from collections import Counter

def decode_message(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return

   
    num_lines = len(lines)
    if num_lines == 0:
        print("The file is empty.")
        return

    if num_lines <= 12:
        meeting_time = f"{num_lines} AM"
    else:
        hour = num_lines % 12
        hour = hour if hour != 0 else 12
        meeting_time = f"{hour} PM"

    
    all_words = []
    for line in lines:
        
        line_clean = line.translate(str.maketrans('', '', string.punctuation)).lower()
        words = line_clean.split()
        all_words.extend(words)

    if not all_words:
        print("No words found in the file.")
        return

    word_counts = Counter(all_words)
    most_common_word, _ = word_counts.most_common(1)[0]

    # Format output
    print(f"Meeting time: {meeting_time}")
    print(f"Meeting place: {most_common_word.capitalize()} Street")

decode_message("Sample.txt")

# Tech Module: Exception Handling
''' You had saved the items and their price details in a text file, which you purchased yesterday from a nearby super market.
You need to know:
1. How many items did you purchase?
2. How many items are free?
3. What is the total amount you had to pay?
4. What is the discount amount?
5. What is the final amount did you pay after the discount?
Help yourself by writing a python code to do this. Include necessary code to handle the possible exceptions.
Note:
Data is stored in a text file Purchase-1.txt.
Each line contains one item's details.
Item name and price is separated by a space.
You have to enter the file name during run time.
Sample input 1:
Purchase-1.txt
Chocolate 50
Biscuit 35
Icecream 50
(blank line)
Discount 5
Sample output 1:
Enter the file name: Purchase-1
No of items purchased: 3
No of free items: 0
Amount to pay: 135
Discount given: 5
Final amount paid: 130'''

def analyze_purchases():
    try:
        filename = input("Enter the file name: ").strip()
        if not filename.endswith(".txt"):
            filename += ".txt"

        with open(filename, "r") as file:
            lines = file.readlines()

        total_items = 0
        free_items = 0
        total_amount = 0
        discount = 0

        for line in lines:
            line = line.strip()
            if not line:
                continue  

            parts = line.split()
            if len(parts) == 2:
                item, price_str = parts
                if item.lower() == "discount":
                    try:
                        discount = int(price_str)
                    except ValueError:
                        print(f"Invalid discount value: {price_str}")
                        continue
                else:
                    try:
                        price = int(price_str)
                        total_items += 1
                        if price == 0:
                            free_items += 1
                        total_amount += price
                    except ValueError:
                        print(f"Invalid price for item '{item}': {price_str}")
                        continue
            else:
                print(f"Invalid line format: '{line}'")
                continue

        final_amount = total_amount - discount

        print(f"No of items purchased: {total_items}")
        print(f"No of free items: {free_items}")
        print(f"Amount to pay: {total_amount}")
        print(f"Discount given: {discount}")
        print(f"Final amount paid: {final_amount}")

    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

analyze_purchases()


