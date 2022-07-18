
print("***************** WELCOME TO STUDENT MANAGEMENT SYSTEM *****************")
global l
l=["Shanti", "Sonam", "Ram", "Raj", "Aman", "Priya", "Barbie", "Kajal"]

def view_list():
    for i in range(len(l)):
        print(l[i])

def add_name():
    name=input("\nEnter the name:")
    l.append(name)
    print("Student name added successfully...")

def del_name():
    name=input("\nEnter the name to be deleted:")
    if name in l:
        l.remove(name)
        print("Student name deleted successfully...")
    else:
        print("Student not found...")

def search():
    name=input("\nEnter the name to search:")
    if name in l:
        print("Student name found in record...")
    else:
        print("Student not found...")

while True:
    print("Choose any option:\n")
    print("1. Display the list")
    print("2. Add names to the list")
    print("3. Delete names from the list")
    print("4. Search any name from the list")
    print("5. Exit")

    ch=int(input("\nEnter your choice:"))

    if ch==1:
        view_list()

    elif ch==2:
        add_name()

    elif ch==3:
        del_name()

    elif ch==4:
        search()

    elif ch==5:
        exit()
    else:
        print("Wrong input")

    g=input("Do you want to continue(y/n):")
    print("_________________________________")

    if (g=="y"):
        continue
    elif (g=="n"):
        break
    

    

    

