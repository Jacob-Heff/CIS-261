# Jacob Heffington
# CIS261
# Invoice Line-Item Calculator

def getPrice():
    while(True): 
        try:
            price = float(input("Enter price: "))
            break
        except:
            print("Invalid decimal number. Please try again.")
    return price

def getQuantity():
    while(True): 
        try:
            quantity = int(input("Enter quantity: "))
            break
        except:
            print("Invalid integer. Please try again.")
    return quantity

def main():
    fb = ""
    print("The Invoice Line Item Calculator")

    while(True):
        print("")        

        price = getPrice()
        quantity = getQuantity()

        total = price*quantity
        
        txt = "\nPRICE: {P:.2F}"
        print(txt.format(P = price))
        
        print("QUANTITY:", quantity)
        
        txt = "TOTAL: {T:.2F}"
        print(txt.format(T = total))
    
        fb = input("Enter another line item? (y/n)")
        if fb == "n":
            print("\nBye!")
            break
    
if __name__ == "__main__":
        main()