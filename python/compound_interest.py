"""
Compound Interest Calculator Function

Objective:
Write a function named 'compound_interest_calculator' to calculate compound interest.

Function Parameters:
1. P (float): Principal amount.
2. r (float): Annual interest rate in decimal.
3. n (integer): Number of times interest is compounded per year.
4. t (integer): Number of years for investment.

Instructions:
- Use the formula: A = P(1 + r/n)^(nt) to calculate compound interest.
- Return the accumulated amount A after t years.
- Handle edge cases for inputs.

Example Test Cases:
1. compound_interest_calculator(1000, 0.05, 12, 5) should calculate the amount.
2. compound_interest_calculator(500, 0.07, 4, 10) should calculate the amount.
3. compound_interest_calculator(1500, 0.03, 6, 7) should calculate the amount.
"""


def compound_interest_calculator(P, r, n, t):
    # Your code goes here
    # Implement the compound interest calculation
    pass  # Delete this after implementing some code inside this function


# Test cases
print(compound_interest_calculator(1000, 0.05, 12, 5))  # Expected: Amount after 5 years
print(compound_interest_calculator(500, 0.07, 4, 10))  # Expected: Amount after 10 years
print(compound_interest_calculator(1500, 0.03, 6, 7))  # Expected: Amount after 7 years


def compound_interest_calculator(P, r, n, t):
    # Check for edge cases
    if P <= 0 or r < 0 or n <= 0 or t <= 0:
        return "Invalid input. Please provide valid positive values for all parameters."

    # Calculate compound interest using the formula
    A = P * (1 + r/n)**(n*t)
    
    return A

principal_amount = 1000.0
annual_interest_rate = 0.05  # 5%
compounding_frequency = 12  # Monthly compounding
investment_years = 5

result = compound_interest_calculator(principal_amount, annual_interest_rate, compounding_frequency, investment_years)

print(f"The accumulated amount after {investment_years} years is: ${result:.2f}")

def compound_interest_calculator(P, r, n, t):
    # Check for edge cases
    if P <= 0 or r < 0 or n <= 0 or t <= 0:
        return "Invalid input. Please provide valid positive values for all parameters."

    # Calculate compound interest using the formula
    A = P * (1 + r/n)**(n*t)
    
    return A

principal_amount = 500
annual_interest_rate = 0.07  # 5%
compounding_frequency = 4  # Monthly compounding
investment_years = 10

result = compound_interest_calculator(principal_amount, annual_interest_rate, compounding_frequency, investment_years)

print(f"The accumulated amount after {investment_years} years is: ${result:.2f}")

def compound_interest_calculator(P, r, n, t):
    # Check for edge cases
    if P <= 0 or r < 0 or n <= 0 or t <= 0:
        return "Invalid input. Please provide valid positive values for all parameters."

    # Calculate compound interest using the formula
    A = P * (1 + r/n)**(n*t)
    
    return A

principal_amount = 1500
annual_interest_rate = 0.03 
compounding_frequency = 6  # Monthly compounding
investment_years = 7

result = compound_interest_calculator(principal_amount, annual_interest_rate, compounding_frequency, investment_years)

print(f"The accumulated amount after {investment_years} years is: ${result:.2f}")



