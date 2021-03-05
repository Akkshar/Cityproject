print("Hi! This is a program that will tell you the main cities in a continent")
print("that you choose\nbased on: area, population")
print("⚠️dont type in any typos please!⚠️")

def cities():
    continent = input("please any continent (Asia, Africa, Europe, North america, South america):-")
    file = open(continent,'r')
    num = 0
    ans = 0
    for var in file:
        words = var.split('\n')
        num = num+len(words)
    print(words)
    num = input("Do you want to know any information about any city (y/n)")
    
cities()
