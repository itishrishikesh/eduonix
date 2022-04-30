y = 'Y'

while y == 'Y':
    try:
        X = int(input("\nEnter First Number: "))
        Y = int(input("\nEnter Second Number: "))

        OPERATION = input("ENTER OPERATION? (ADD/SUB/DIV/MUL): ")

        if OPERATION == "ADD":
            print(str(X+Y))
        elif OPERATION == "SUB":
            print(str(X-Y))
        elif OPERATION == "DIV":
            print(str(X/Y))
        elif OPERATION == "MUL":
            print(str(X*Y))
        else:
            print("\nEnter a correct option!")
    except:
        print("\nyou entered invalid operands!!")

    y = input("\nDo you want another try? (Y/N)")