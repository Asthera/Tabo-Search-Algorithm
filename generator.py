import random

#Function which reopen file and write in it new tsp with NumberPoints and random price (StartPrice,EndPrice)

def generate(NumberPoints,StartPrice,EndPrice):
    f = open("/Users/volodimir/Downloads/input.txt", 'w')
    for i in range(1, NumberPoints + 1):
        for j in range(i + 1, NumberPoints + 1):
            weight = random.randint(StartPrice,EndPrice)
            f.write(str(i) + ' ' + str(j) + ' ' + str(weight) + '\n')
    f.close()
