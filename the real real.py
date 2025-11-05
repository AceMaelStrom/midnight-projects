import random
import numbers
import time
import math
def randomidear(intergrad):
    boundsstart = random.randint(-20,0)
    boundend = random.randint(0,20)
    bounds = []
    bounds.append(boundsstart)
    bounds.append(boundend)
    intergrad =float(intergrad)
    if int(intergrad) > boundsstart and int(intergrad) < boundend:
        bounds.insert(1,intergrad)
        print(str(bounds))
    

def randomnumber(starting,ending):
    number = random.randint(starting,ending)
    if number <= 0:
        print("lower than a natural number, LOL "+ str(number))
    else:
        print("higher huh? "+ str(number))

def bracketrandomcomposite(containingnumber):
    randomidear(int(input()))
    bracketrand = randomnumber(int(input()),str(int(input)))
    for value in bracketrand:
        if value <= containingnumber:
            print("wow, your set isnt greater than "+containingnumber)
        else:
            print("it's bigger than "+containingnumber+"!")
            
def greatness(greatfactor):
    greatbracket =[]
    for i in range(int(greatfactor)+1):
        greatbracket.append(i)
    return greatbracket

def textnumber(inputnumber):
    a= int(inputnumber)*random.randint(1,20)
    b= {greatness(input())}
    multarray = {b*i for i in a}
    print(multarray)
    
def loadingbar(size):
    timesize = size *0.1
    for i in range(1,int(size)+1):
        timebar = "[" + "#" * i +"-" *(int(size)-i) + "]"
        time.sleep(timesize)
        print(timebar)
        timesize = timesize * 0.65
    print("loaded")

thegreatvalue = (str(greatness(input())))
print(thegreatvalue)

loadingbar(int(input()))

