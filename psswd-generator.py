import random, string

def gen_passwd():
    result = ""
    symbols = ['!', '#', '$', '%', '&', '*', '+']

    for i in range(0, 3):
        result = result + random.choice(string.ascii_letters)
        result = result + str(random.randint(0, 9))
        result = result + random.choice(symbols)
    
    result = list(result)
    random.shuffle(result)
    
    return ''.join(result)

y = 'Y'

while y == 'Y':
    print("\nHere's a Password for you:")
    print(gen_passwd())
    y = input("\nDo you want another password? (Y/N)")