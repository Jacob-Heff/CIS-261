# Jacob Heffington
# CIS261
# Movie Guide Part 2

def display():
    print("The Movie List Program")
    print("")
    print("COMMAND MENU")
    print("list - List all movies")
    print("add - Add a movie")
    print("del - Delete a movie")
    print("exit - Exit program")
    
def getMovieTitles():
    l = open('movies.txt').read().splitlines()
    return l

def writeMovieTitles(lst):
    with open('movies.txt', 'w') as f:
        for line in lst:
            f.write(f"{line}\n")

def displayTitles(l):
    for i in range(0, len(l)):
        num = str(i+1)
        print(num + ". " + l[i])

def addTitle(lst,name):
    lst.append(name)
    writeMovieTitles(lst)

def deleteTitle(lst,num):
    lst.pop(num)
    writeMovieTitles(lst)

def main():
    display()
    lst = getMovieTitles()
    while True:
        print("")
        command = input("Command: ")
        if command == "list":
            displayTitles(lst)
        elif command == "add":
            name = input("Name: ")
            addTitle(lst,name)
            print(name,"was added.")
        elif command == "del":
            num = int(input("Number: "))
            if len(lst) >= num:
                print(len(lst),num)
                print(lst[num-1], "was deleted.")
                deleteTitle(lst,num-1)
            else:
                print("Invalid movie number.")
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Not a valid command. Please try again.")
                                                                                                                                                                                                                                                                                                                                                                                                
if __name__ == "__main__":
    main()