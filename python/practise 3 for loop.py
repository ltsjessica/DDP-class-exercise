breakfast=["egg", "sandwich", "burger","tuna"]
for meal in breakfast:
    print(meal)

breakfast=["egg", "sandwich", "burger","tuna"]
for meal in breakfast:
    if meal == "burger":
        break
    print (meal)

breakfast=["egg", "sandwich", "burger","tuna"]
for meal in breakfast:
    if meal == "burger":
        continue
    print (meal)

breakfast=["egg", "sandwich", "burger","tuna"]
drinks=["coffee","milktea","soya"]
number=0
for meal in breakfast:
    for beverage in drinks:
        print(f"{meal}and{drinks}")
        number += 1
    print(f"total {number} of combination") 



