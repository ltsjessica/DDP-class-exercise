Steak=100
Chicken=200
Pork=300
print(not Steak==Chicken) 
print(Steak>Chicken or Pork>Steak)
print(Steak>Chicken and Pork>Chicken)

if Steak>Chicken:
    print("steak is more expensive than chicken")
else:
    print("chicken is more expensive than steak")

Ordering = input ("What would you prefer? (A)steak (B)chicken : ").upper()
if Ordering == "A":
    if set == "Y":
        print(f"the price for upgrade is {Steak+Chicken}")
else: 
    print(f"the price of steak is {Steak}")

if Ordering == "B":
    if set == "W":
        print(f"the price for upgrade is {Steak+Chicken}")
else: 
    print(f"the price of pork is {Pork}")