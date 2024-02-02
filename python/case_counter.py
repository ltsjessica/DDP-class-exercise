"""
Letter Case Counter Function

Objective:
Write a function named 'case_counter' that counts the number of uppercase and lowercase letters in a given string.

Function Parameter:
text (string): The string in which the letters need to be counted.

Instructions:
- The function should calculate and print two numbers: the count of uppercase letters and the count of lowercase letters in the string.
- If there are no letters of a particular case (uppercase or lowercase) in the string, the function should print 0 for that case.
- Non-alphabetic characters in the string should be ignored and not counted.

Example Test Cases:
1. case_counter("Hello World!") should print the counts of uppercase and lowercase letters.
2. case_counter("PYTHON") should print the counts of uppercase and lowercase letters.
3. case_counter("python") should print the counts of uppercase and lowercase letters.
4. case_counter("1234!@#$") should print 0 for both counts.
"""


def case_counter(text):
    uppercase_count=0
    lowercase_count=0

    for char in text:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count +=1 
    print ("upperletter:", uppercase_count)
    print ( "lowercase letters:", lowercase_count)

def case_counter(text):
    uppercase_count=0
    lowercase_count=0

    for char in text:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count +=1 

    print ("upperletter:", uppercase_count)
    print ( "lowercase letters:", lowercase_count)

def case_counter(text):
    uppercase_count=0
    lowercase_count=0

    for char in text:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count +=1 

    print ("upperletter:", uppercase_count)
    print ("lowercase letters:", lowercase_count)

def case_counter (text):
    uppercase_count=0
    lowercase_count=0

    for char in text:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count +=1 

    print ("upperletter:", uppercase_count)
    print ("lowercase letters:", lowercase_count)

    # Remember to count uppercase and lowercase letters and ignore non-alphabetic characters
    pass  # Delete this after implementing some code inside this function.


# Test cases
case_counter("Hello World!")  # Expected: Uppercase letters: 2, Lowercase letters: 8
case_counter("PYTHON")  # Expected: Uppercase letters: 6, Lowercase letters: 0
case_counter("python")  # Expected: Uppercase letters: 0, Lowercase letters: 6
case_counter("1234!@#$")  # Expected: Uppercase letters: 0, Lowercase letters: 0



def case_counter(text):
    # Initialize counters for uppercase and lowercase letters
    uppercase_count = 0
    lowercase_count = 0
    
    # Iterate through each character in the string
    for char in text:
        # Check if the character is an uppercase letter
        if char.isupper():
            uppercase_count += 1
        # Check if the character is a lowercase letter
        elif char.islower():
            lowercase_count += 1
    
    # Print the results
    print("Uppercase letters:", uppercase_count)
    print("Lowercase letters:", lowercase_count)

# Example usage:
input_text = "Hello World! 123"
case_counter(input_text)
