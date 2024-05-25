# Jacob Heffington
# CIS261
# Country

def display():
    print("COMMAND MENU")

    print("view - View country name")
    print("add - Add a country")
    print("del - Delete a country")
    print("exit - Exit program")
    print()

def createDict():
    cDict = {"CA": "Canada", "DE": "Germany", "US": "United States"}
    return cDict
        
def viewCountry(cDict):
    codes = list(cDict.keys())
    codes_line = "Country codes: "
    i=0
    for code in codes:
        i+=1
        if i == len(codes):
            codes_line += code
        else:
            codes_line += code + ", "
    print(codes_line)
    code = input("Enter country code: ")
    code = code.upper()
    if code in cDict:
        name = cDict[code]
        print(f"Country name: {name}")
    else:
        print("There is no country with that code.")
        
def addCountry(cDict):
    code = input("Enter country code: ")
    code = code.upper()
    if code in cDict:
        name = cDict[code]
        print(f"{name} is already using this code.")
    else:
        name = input("Enter country name: ")
        name = name.title()
        cDict[code] = name
        print(f"{name} was added.")
        
def deleteCountry(cDict):
    code = input("Enter country code: ")
    code = code.upper()
    if code in cDict:
        name = cDict.pop(code)
        print(f"{name} was deleted.")
    else:
        print("There is no country with that code.")
        
def main():
    display()
    cDict = createDict()
    while True:
        print("")
        command = input("Command: ")
        if command == "view":
            viewCountry(cDict)
        elif command == "add":
            addCountry(cDict)
        elif command == "del":
            deleteCountry(cDict)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Not a valid command. Please try again.")
            
if __name__ == "__main__":
    main()