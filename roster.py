import os
import sys
import urllib.request


def clearscr():
    if os.name == 'nt':
        os.system("cls")
    elif os.name == 'posix':
        os.system("clear")
    else:
        print('bruh what system are you using')


def initPlan():
    global replace
    print("Loading...")
    try:
        _ = open('roster.plan', "w").close()
        fileCurrent = open('roster.plan', "r+")
        currentPath = __file__
        url = "https://raw.githubusercontent.com/CompactLethargy13/Australia-Trip/main/roster.plan"
        newfilepath, _ = urllib.request.urlretrieve(url, filename=currentPath)
        newFile = open(str(newfilepath), "r+")
        lists = fileCurrent.readlines()
        listToReplace = newFile.readlines()
        c = 0
        for i in lists:
            for j in listToReplace:
                Replacement = i.replace(i, j)
                replace = Replacement
            c += 1
        fileCurrent.seek(0)
        fileCurrent.truncate()
        fileCurrent.writelines(replace)
        fileCurrent.close()
    except:
        print("Something went wrong. Check your internet connection")
    clearscr()


# TODO FIX CERTAIN VERY OBVIOUS PROBLEMS

class Roster:
    def __init__(self, plannerList, plannerFile):
        self.roster = plannerList
        self.file = plannerFile

    def saveChanges(self):
        self.file.seek(0)
        self.file.truncate()
        for i in roster:
            self.file.write(i)

    def showItems(self):
        print('Your items: \n')
        if len(self.roster) != 0:
            for items in self.roster:
                print(items, end='')
        else:
            print("None yet\n")

    def newItem(self, num):
        name = input("Input the name of the item\n\t>> ")

        while True:
            date = input("Input the date that the item occurs in DD/MM/YY format\n\t>> ")
            datelist = [i for a, i in enumerate(date)]
            try:
                if datelist[2] != '/' and datelist[5] != '/':
                    print("Please input the date in the correct format. ")
                    continue

                if len(datelist) != 8:
                    print("Please input the date in the correct format")
                    continue
            except IndexError:
                print("Please input the date in the correct format. ")
                continue
            break

        while True:
            time = str(input("Input the time of the item in HH:MM format\n\t>> "))
            timelist = [i for a, i in enumerate(time)]
            try:
                if timelist[2] != ':' or len(timelist) != 4:
                    print("Please input the time in the correct format. ")
                    continue
            except IndexError:
                print("Please input the time in the correct format. ")
                continue
            if time == '25:00':
                time = 'undefined'
            break

        string = ""
        string += "Item "
        string += str(int(num+1))
        string += "\n"
        string += "Name: "
        string += name
        string += "\n"
        string += "Date: "
        string += date
        string += "\n"
        string += "Time: "
        string += time
        string += "\n\n"

        self.roster.append(string)
        print("Item " + name + " added")

    def clearFile(self):
        confirm = input("ARE YOU SURE YOU WANT TO CLEAR THE FILE\nTHIS CANNOT BE UNDONE\n>> ")
        if confirm == 'y':
            self.file.seek(0)
            self.file.truncate()
            self.roster = []
            print("Data cleared")
        else:
            print("Your data survives. ")


# calling main file, should not be edited
# write mode is called to make a new file in case it hasn't been made
try:
    plan = open('roster.plan', 'r+')
except FileNotFoundError:
    deez = open('roster.plan', 'w').close()
    plan = open('roster.plan', 'r+')

# main variable where edits are made
roster = plan.readlines()

clearscr()

Roster = Roster(roster, plan)
Roster.__init__(roster, plan)

print('Your items: \n')
if len(roster) != 0:
    for item in roster:
        print(item, end='')
else:
    print("None yet\n")
    inityes = input("Do you want to sync with the plan on github? (y/n): ")
    if inityes == 'y':
        initPlan()

while True:
    print('''Actions:
    1: Print items
    2. New item
    3. Clear all items (CANNOT BE UNDONE)
    4. Quit program
    NOTE: USE QUIT PROGRAM TO QUIT OR CHANGES WILL NOT BE SAVED''')
    choice = input(">> ")
    if choice == '1':
        Roster.showItems()
    elif choice == '2':
        Roster.newItem(len(roster) / 6)
        Roster.saveChanges()
    elif choice == '3':
        Roster.clearFile()
        Roster.saveChanges()
    elif choice == '4':
        break
    else:
        clearscr()
        print("Invalid input. \nPlease input a number from 1 to 3. ")
        pass
print("Saving data...")
Roster.saveChanges()
# plan.close()
print("Data saved. ")
sys.exit()
