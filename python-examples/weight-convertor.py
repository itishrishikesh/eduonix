y = 'Y'

while y == 'Y':
    try:
        unit = input("Convert from KG or Pound?: ")

        weight = float(input("What's you weight?: "))

        if unit == "KG":
            print(str((2.205)*weight))
        elif unit == "Pound":
            print(str(weight/(2.205)))
        else:
            print("Invalid Option selected!")
    except:
        print("Invalid operation!")
    finally:
        y = input("\nDo you want another password? (Y/N)")