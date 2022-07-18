print("************************** Banking System **************************")

global data
data={}

list1=["Name", "Address", "Government ID", "phone no", "Account type", "Amount"]

list2=[]

def input_data():
    acc_no=input("Enter Account number:")

    for item in list1:
        list2.append(input("Enter %s :"%item))

    data[acc_no]=dict(zip(list1,list2))
    print("Account created successfully...")


def input_details():
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdrawl")
    ch=int(input("\nEnter your choice:"))

    if ch==1:
        print("Available balance:",data[acc_no]["Amount"])

    elif ch==2:
        deposit=int(input("Enter amount to be deposited:"))
        deposit+=data["Amount"]
        print("Amount successfully deposited")
        print("Available balance:", deposit)

    elif ch==3:
        withdrawl=int(input("Enter amount to be withdrawl:"))
        withdrawl-=data["Amount"]
        print("Amount Withdrawl successfully")
        print("Available balance:",withdrawl)

    else:
        print("Wrong input")


while True:
    print("Choose any option:\n")
    print("1. New customer")
    print("2. Existing customer")
    print("3. Exit")

    op=int(input("\nEnter your Choice:"))

    if op==1:
        input_data()
        
    elif op==2:
        acc_no=input("\nEnter account number:")
        if acc_no in data:
                       input_details()
        else:
            print("Account doesnot exist")

    elif op==3:
        exit()

    else:
        print("Wrong input")

    g=input("Do you want to continue(y/n):")
    print("_________________________________")

    if (g=="y"):
        continue
    elif (g=="n"):
        break
    



        
