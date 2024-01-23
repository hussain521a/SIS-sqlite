import sqlite3

#Simple Student Information System using Python and sqlite3 

#Define connection and cursor
connection = sqlite3.connect('SIS.db')
cursor = connection.cursor()

#Create table
cursor.execute("CREATE TABLE IF NOT EXISTS student(id integer PRIMARY KEY, first_Name text, last_Name text, age integer, gender text)")

#Create menu
def printMenu(): 
    print("-MENU-")
    print("0. EXIT")
    print("1. GET ALL STUDENTS")
    print("2. GET ONE STUDENT")
    print("3. ADD A STUDENT")
    print("4. EDIT A STUDENT")
    print("5. DELETE A STUDENT")
    print("")
    
#Exit program
def exit():
    return False

#Get all students
def getAll():
    for row in cursor.execute("SELECT id, first_Name, last_Name, age, gender FROM student ORDER BY id"):
        print(row)
    print("There are "+str(highestID)+" ids.")
        
#Get one student
def getOne():
    check_id = 1
    idVal=input("What id do you want? (Range: 1-"+str(highestID)+")\nInput:")
    for row in cursor.execute("SELECT id, first_Name, last_Name, age, gender FROM student ORDER BY id"):
        if check_id == int(idVal):
            print("")
            print("Student with the id "+str(check_id)+" is "+str(row))
        check_id = check_id+1

#Add a new student
def add():
    firstName = input("What is the first name?\nInput:")
    lastName = input("What is the last name?\nInput:")
    age = input("What is the age?\nInput:")
    gender = input("What is the gender?\nInput:")
    data = (int(highestID)+1, firstName, lastName, int(age), gender)
    cursor.execute("INSERT INTO student (id, first_Name, last_Name, age, gender) VALUES(?, ?, ?, ?, ?)", data)
    connection.commit()
    
#Edit existing student
def edit():
    chooseID = input("Which ID would you like to edit? (Range: 1-"+str(highestID)+")\nInput:")
    firstName = input("What is the new first name?\nInput:")
    lastName = input("What is the new last name?\nInput:")
    age = input("What is the new age?\nInput:")
    gender = input("What is the new gender?\nInput:")
    cursor.execute("UPDATE student SET first_Name = (?) WHERE id = (?)", (firstName, chooseID))
    cursor.execute("UPDATE student SET last_Name = (?) WHERE id = (?)", (lastName, chooseID))
    cursor.execute("UPDATE student SET age = (?) WHERE id = (?)", (age, chooseID))
    cursor.execute("UPDATE student SET gender = (?) WHERE id = (?)", (gender, chooseID))
    connection.commit()
    print("Updated student in id "+str(chooseID))
    
    
#Delete existing student
def delete():
    chooseID = input("Which ID would you like to delete? (Range: 1-"+str(highestID)+")\nInput:")
    cursor.execute("DELETE FROM student WHERE id IN (?)", [int(chooseID)])
    connection.commit()
    print("Deleted student with id of "+str(chooseID))



#Main program
print("Welcome to SIS\n")
run = True
while run == True:
    printMenu()
    highestID = 0
    for row in cursor.execute("SELECT first_Name, last_Name, age, gender FROM student ORDER BY id"):
        highestID = highestID+1
    action = input("What would you like to do?\nInput:")
    if action == '0':
        run = exit()
    else:
        if action == '1':
            getAll()
            print("")
        elif action == '2':
            getOne()
            print("")
        elif action == '3':
            add()
            print("")
        elif action == '4':
            edit()
            print("")
        elif action == '5':
            delete()
            print("")