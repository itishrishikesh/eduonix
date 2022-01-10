import random, string

def gen_passwd():
    result = ""
    symbols = ['!', '#', '$', '%', '&', '*', '+']

    for i in range(0, 10):
        result = result + random.choice(string.ascii_letters)
        result = result + str(random.randint(0, 9))
        result = result + random.choice(symbols)
    
    result = list(result)
    random.shuffle(result)
    
    return ''.join(result)

print(gen_passwd())