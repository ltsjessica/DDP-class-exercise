
mobile1={ 
    "brand" : "apple",
    "model" : "iPhone14Pro",
    "volume" : "512GB",
    "color" : "purple"
} 
mobile2={
    "brand" : "samsung",
    "model" : "galaxy s22 ultra",
    "volume" : "512GB",
    "color" : "red"
}
mobile3={
    "brand" : "apple",
    "model" : "iPhone 15",
    "volume" : "512GB",
    "color" : "blue"
}
stock=[mobile1, mobile2, mobile3]
enquiry=input("please enter the enquired brand name")
if enquiry in str(stock):
    print (stock) 
else: 
    print ("no stock")

stock=[mobile1, mobile2, mobile3]
enquiry=input("please enter the enquired brand name")
if enquiry in str(stock):
    for mobile in stock:
        if mobile["model"] == enquiry:
            print(f"it has stock{mobile['color']}, {mobile['brand']}, {mobile['volume']}")
else: 
    print (f"there is no{enquiry}stock")

