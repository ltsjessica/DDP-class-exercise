table = [1,2,3,4,5,6]
product = 1
for number in table:
    product *= number
print(product)


table = [1,2,3,4,5,6]
list=[]
for number in table:
    if number>3:
        list.append(number)
print(list)


table = [1,-2,3,-4,5,-6]
positivenumber=[]
negativenumber=[]
for number in table:
    if number>0:
        positivenumber.append(positivenumber)
    else:
        negativenumber.append(number)
print(f"positive number include{positivenumber}")
print(f"negative number include{negativenumber}")