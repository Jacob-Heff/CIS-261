# Jacob Heffington
# CIS261
# Movie Guide Part 1

def display():
    print("The Movie List Program")
    print("")
    print("COMMAND MENU")
    print("list - List all movies")
    print("add - Add a movie")
    print("del - Delete a movie")
    print("exit - Exit program")
    
def movieTitles():
    l = ["Five Nights at Freddies","Barbie","Oppenhiemer"]
    return l

def displayTitles(l):
    for i in range(0, len(l)):
        num = str(i+1)
        print(num + ". " + l[i])

def addTitle(lst,name):
    lst.append(name)
    return lst

def deleteTitle(lst,num):
    lst.pop(num)
    return lst

def main():
    display()
    lst = movieTitles()
    while True:
        print("")
        command = input("Command: ")
        if command == "list":
            displayTitles(lst)
        elif command == "add":
            name = input("Name: ")
            lst = addTitle(lst,name)
            print(name,"was added.")
        elif command == "del":
            num = int(input("Number: "))-1
            if len(lst) >= num:
                print(lst[num],"was deletd.")
                lst = deleteTitle(lst,num)
            else:
                print("Invalid movie number.")
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Not a valid command. Please try again.")
            
if __name__ == "__main__":
    main()