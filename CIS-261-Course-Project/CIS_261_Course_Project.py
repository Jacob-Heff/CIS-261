import datetime

class Login():
    def __init__(self, user, password, authorization):
        self.user = user
        self.password = password
        self.authorization = authorization
        
def createUsers():
    users = []
    with open('users.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, pwd, auth = data.split("|")
            users.append(user)
            
    while True:
        user = input("Username: ")
        if user.lower() == "end":
            break
        for i in users:
            if i != user:
                break
        pwd = input("Password: ")
        while True:
            auth = input("Authorization(Admin or User): ")
            if auth.lower() in ("admin", "user"):
                break
        with open('users.txt', 'a') as f:
            f.write(user + "|" + pwd + "|" + auth + "\n")
            
def login():
    userInfo = []
    userInfoList = []
    with open('users.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, pwd, auth = data.split("|")
            userInfo = (user, pwd, auth)
            userInfoList.append(userInfo)
    
    while True:
        user = input("Username: ")
        pwd = input("Password: ")
        for userInfo in userInfoList:
            if user == userInfo[0]:
                print(user, userInfo[0])
                if pwd == userInfo[1]:
                    current_user = Login(userInfo[0], userInfo[1], userInfo[2])
                    return current_user
                else:
                    print("Wrong Password")
                    quit()
        print("Wrong Username")
        quit()

def displayUsers():
    with open('users.txt', 'r') as f:
        first_char = f.read(1) # Get the first character
        if not first_char:
            print("No accounts exist") #
        else:
            f.seek(0)
            for line in f.readlines():    
                data = line.rstrip()
                user, pwd, auth = data.split("|")
                print("Username:", user, "Password:", pwd, "Authorization:",auth )
def addToFile(details):
    """
    Adds the infomation from the employee details list to the file.
    """
    with open('employees.txt', 'a') as file:
        for (i, detail) in enumerate(details):
            if i != len(details)-1:
                file.write(detail + "|" )
            else:
                file.write(detail + "\n")
            
def getDates():
    """
    Requests the from and to dates for the hours worked, and then checks them to ensure that they agree with formatting requirements
    """
    f = input("From Date (mm/dd/yyyy):")
    f = checkDate(f, "From Date(mm/dd/yyyy):")
    t = input("To Date (mm/dd/yyyy):")
    t = checkDate(t, "To Date(mm/dd/yyyy):")
    return f, t

def checkDate(date, input_request):
    """
    Uses the datetime strptime function to ensure that the function meets the mm/dd/yyyy format requirements, if it doesn't, it asks the user to resubmit
    """
    while True:
        try:
            datetime.datetime.strptime(date,"%m/%d/%Y")
            break
        except:
            date = input(input_request)
    return date

def getName():
    """
    Requests the employee name from user and returns it
    """
    n = input("Employee Name: ")
    return n

def getHours():
    """
    Requests the total hours for the employee from user and returns it
    """
    h = input("Total Hours: ")
    return h

def getHourlyRate():
    """
    Requests the hourly rate for the employee from user and returns it
    """
    r = input("Hourly Rate: ")
    return r

def getTaxRate():
    """
    Requests the tax rate for the employee from user and returns it
    """
    t = float(input("Tax Rate: "))
    t = t/100
    return str(t)

def getGross(t, r, tr):
    """
    Takes the total hours, hourly rate, and tax rate
    Calculates and returns the gross pay, income tax and net pay
    """
    g = t*r
    i = g*tr
    n = g-i
    return g, i, n

def display(empDetailList):
    """
    Pulls the data from the employee detail list and displays it to the user, updating the dictionary totals for each item in the list
    """
    te = 0.00 #Tracks total employees
    th = 0.00 #Tracks total hours
    tg = 0.00 #Tracks total gross pay
    tt = 0.00 #Tracks total taxes
    tn = 0.00 #Tracks total net pay
    for empList in empDetailList:
        f = empList[0]
        t = empList[1]
        n = empList[2]
        h = empList[3]
        hr = empList[4]
        tr = empList[5]
        
        # Calculates the gross pay, income tax, and net pay
        g, i, np = getGross(h, hr, tr)
        
        print("From Date:",f,"|","To Date:",t,"|","Employee:",n,"|",
              f'Hours Worked: {h}',"|",f'Gross Pay: {g}',"|",
              f'Tax Rate: {tr}',"|",f'Net Pay: {n}'+"\n")
        
        #Updates totals for new employee data
        te += 1
        th += h
        tg += g
        tt += i
        tn += np
        
        empTotals["totEmp"] = te
        empTotals["totHours"] = th
        empTotals["totGross"] = tg
        empTotals["totTax"] = tt
        empTotals["totNet"] = tn

def displayTotals(empTotals):  
    """
    Pulls the data from the employee totals dictionary and displays it to the user.
    """
    print(f'Total Number Of Employees: {empTotals["totEmp"]}')
    print(f'Total Hours Of Employees: {empTotals["totHours"]}')
    print(f'Total Gross Pay Of Employees: {empTotals["totGross"]}')
    print(f'Total Tax Of Employees: {empTotals["totTax"]}')
    print(f'Total Net Pay Of Employees: {empTotals["totNet"]}')
    print("")
            
def getReport():
    """
    Asks the user for the dates they would like to generate a view for, and then displays the relevent data
    """
    date = input("From Date to View or 'All' to view all dates:").lower() #Collects a date to index for
    while True:
        # Checks to see if the input is a valid date or if its "all". 
        # If it is a valid date, it breaks the loop and processes for those dates
        # If it is "all", it prints all data from the file, by adding it to the empDetail list and running it through the display functions and then ending the function with a return None
        # If it is neither, it requests a new date from the user.
        try:
            datetime.datetime.strptime(date,"%m/%d/%Y")
            break
        except:
            if date == "all":
                with open('employees.txt', 'r') as f:
                    for line in f.readlines():
                        data = line.rstrip()
                        f, t, n, h, hr, tr = data.split("|")
                        empDetail = []
                        empDetail.insert(0, f)
                        empDetail.insert(1, t)
                        empDetail.insert(2, n)
                        empDetail.insert(3, float(h))
                        empDetail.insert(4, float(hr))
                        empDetail.insert(5, float(tr))
                        empDetailList.append(empDetail)
                print("")
                display(empDetailList)
                print("")
                displayTotals(empTotals)
                return None
            date = input("From Date to View or 'All' to view all dates:").lower()
    with open('employees.txt', 'r') as f:
        #Checks each line in the txt file, if the from date is equal to the date requested, it adds it to the list, it then uses the display functions to display the data
        for line in f.readlines():
            data = line.rstrip()
            f, t, n, h, hr, tr = data.split("|")
            if f == date:
                empDetail = []
                empDetail.insert(0, f)
                empDetail.insert(1, t)
                empDetail.insert(2, n)
                empDetail.insert(3, float(h))
                empDetail.insert(4, float(hr))
                empDetail.insert(5, float(tr))
                empDetailList.append(empDetail)
    print("")
    display(empDetailList)
    print("")
    displayTotals(empTotals)
    
def main():
    while(True): #Gets user inputs until terminated by the user typing "End"
        #Prompts user for End input
        fb = input ("Reply End to end the program or press enter to add a data entry: ")
        if fb.lower() == "end":
            break
        
        f, t = getDates()
        n = getName()
        h = getHours()
        hr = getHourlyRate()
        tr = getTaxRate()

        addToFile((f, t, n, h, hr, tr))
    
if __name__ == "__main__":
    fb = ""
    te = 0  #Tracks total employees
    th = 0 #Tracks total hours
    tg = 0 #Tracks total gross pay
    tt = 0 #Tracks total taxes
    tn = 0 #Tracks total net pay
    empDetailList = []
    empTotals = {}

    #Opens the file, and confirms it's readable, if it isn't, it writes the file and then confirms that it can be read.
    while True:
        try:
            with open('employees.txt', 'r') as file:
                file.read()
            break
        except FileNotFoundError:
            with open('employees.txt', 'w') as file:
                file.write("")
                
    #Opens the file, and confirms it's readable, if it isn't, it writes the file and then confirms that it can be read.
    while True:
        try:
            with open('users.txt', 'r') as file:
                file.read()
            break
        except FileNotFoundError:
            with open('users.txt', 'w') as file:
                file.write("")
    print("Create Users or Administrators(Type 'end' to end)\n")
    createUsers()
    print("\nAccounts\n")
    displayUsers()
    print("\nLogin\n")
    current_user = login()
    if current_user.authorization.lower() == "admin":
        print("\nApplication\n")
        main()    
    print("Data")
    print(f'User Information:\nUsername: {current_user.user}\nPassword: {current_user.password}\nAuthorization: {current_user.authorization}')
    getReport()
   