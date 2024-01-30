def sum(int1, int2):
    ans = int1 + int2 
    return ans

if __name__== "_main_":
    int1 = 2
    int2 = 3
    answer = sum(int1,int2)
    print(answer)

mobile={
    "brand" : "apple",
    "model" : "iPhone14Pro",
    "volume" : "512GB",
    "color" : "purple"
}
mobile["volume"]="256GB"
print (mobile)

mobile["volume"]=["512GB", "256GB"]
print (mobile)

mobile.pop("model")
print (mobile)

mobile.popitem()
print   (mobile)

for specification in mobile.keys():
    print (specification) 
for specification in mobile.values():
    print (specification) 