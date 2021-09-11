print("This is the currency converter program")
choice=input("Enter your choice\n Press 1 to convert indian currency to other \n Press 2 to convert other currency to to indian currency")



if choice=="1":
    with open("currency.txt") as f:
        lines = f.readlines()
        
    currencyDict={}
    for line in lines:
        parsed = line.split("\t")
        currencyDict[parsed[0]]=parsed[1]
    amount=float(input("Enter the amount you want to covert"))
    print("Enter the on of the following currency available")
    [print(item) for item in currencyDict.keys()]
    currency=input("Enter one of the currency")
    print(f"The amount for {amount} indian ruppees to {currency} is {amount*float(currencyDict[currency])}")

elif choice=="2":
    with open("currency.txt") as f:
        lines = f.readlines()
        
    currencyDict={}
    for line in lines:
        parsed = line.split("\t")
        currencyDict[parsed[0]]=parsed[2]
    amount=float(input("Enter the amount you want to covert"))
    print("Enter the on of the following currency available")
    [print(item) for item in currencyDict.keys()]
    currency=input("Enter one of the currency")
    print(f"The amount for {amount}  {currency} in indian ruppees {amount*float(currencyDict[currency])}")
else:
    print("Something went wrong choose your option currectly")