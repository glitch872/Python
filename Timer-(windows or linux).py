import time
import os
print("What system do you have?")
print("````````````````````````")
print("(a) Windows")
print("(b) Linux")
s = input("Selection: ")
if s == "a":
	q = "cls"
if s == "b":
	q = "clear"
else:
	exit
os.system(q)
val = input(":Press |ENTER| key: ")
# type "test" as the input for the above zone to gain access to presets
def convert(a,b,c):
    return a*3600 + b*60 + c;
def timer1(a,b,c,d):
    os.system(q)
    while d in range(1, 46800):
        timer = ' Timer: {:02d}:{:02d}:{:02d}'.format(a, b, c)
        print(timer, end="\r")
        d -= 1
        if c == 0:
            if b == 0:
                a -= 1
                b += 59
                c += 59
            else:
                b -= 1
                c += 59
        else:
            c -= 1
        time.sleep(1)
    time.sleep(d)
    os.system(q)
    x = 0
    while x in range(0, 5):
        print("Time is up")
        time.sleep(1)
        os.system(q)
        time.sleep(1)
        x += 1
        os.system(q)
os.system(q)
y = 0
while y == 0:
    print("Countdown timer")
    print("Options:")
    print("(1) View presets")
    print("(2) Custom")
    print("(3) Exit")
    print("````````")
    s = input("Selection: ")
    if s == "1":
        if val == "test":
            os.system(q)
            print("Presets:")
            print("(1) 1 Minute")
            print("(2) 5 Minutes")
            print("(3) 10 Minutes")
            print("(4) Back")
            print("``````````````")
            sel = input("Selection: ")
            if sel == "1":
                a = 0
                b = 1
                c = 0
                d = convert(a,b,c)
                timer1(a,b,c,d)
            elif sel == "2":
                a = 0
                b = 5
                c = 0
                d = convert(a,b,c)
                timer1(a,b,c,d)
            elif  sel == "3":
                a = 0
                b = 10
                c = 0
                d = convert(a,b,c)
                timer1(a,b,c,d)
            elif sel == "4":
                os.system(q)
                print("Going back")
                time.sleep(1)
                os.system(q)
            else:
                os.system(q)
                print("That was not an option")
                print("Going back")
                time.sleep(1)
                os.system(q)
        else:
            os.system(q)
            print("Not yet implemented")
            time.sleep(1)
            os.system(q)
            print("going back to menu in:")
            z = 5
            while z in range(1, 6):
                count = '{:2d}'.format(z)
                print( count, end="\r")
                z -= 1
                time.sleep(1)
            os.system(q)
    elif s == "2":
        os.system(q)
        print("The Max time limit is 24:59.59")
        a = int(input("Hours: "))
        b = int(input("Minutes: "))
        c = int(input("Seconds: "))
        d = convert(a,b,c)
        timer1(a,b,c,d)
    elif s == "3":
        os.system(q)
        print("Bye")
        time.sleep(1)
        y = 1
    else:
        os.system(q)
        print("That is not an option")
        time.sleep(5)
        os.system(q)
os.system(q)
exit
