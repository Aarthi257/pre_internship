import greet_ as g
import random as r
import math
q=["quit","q"]
quit_msg=["quit","Thanks for using,Bye","Let's meet again,Bye","Bubye","See you again","I'm here if you need my help again"]
greetings=g.greet()
print(greetings,",","Have a good day!. I am CALBOT.I'm here to help you with your calculations")
while 1:
    user_msg = input()
    if user_msg in q:
        n=r.randint(0,len(quit_msg))
        print(quit_msg[n])
        break
    else:
        if 'add' in user_msg:
            split=user_msg.split()
            a1=float(split[1])
            a2=float(split[2])
            print(a1+a2)
        elif 'sub' in user_msg:
            split=user_msg.split()
            a1=float(split[1])
            a2=float(split[2])
            print(a1-a2)
        elif 'mul' in user_msg:
            split=user_msg.split()
            a1=float(split[1])
            a2=float(split[2])
            print(a1*a2)
        elif 'div' in user_msg:
            split=user_msg.split()
            a1=float(split[1])
            a2=float(split[2])
            print(a1/a2)
        elif 'mod' in user_msg:
            split=user_msg.split()
            a1=float(split[1])
            a2=float(split[2])
            print(a1%a2)
        elif 'pow' in user_msg:
            split=user_msg.split()
            a1=float(split[1])
            a2=float(split[2])
            print(pow(a1,a2))
        elif 'sqrt' in user_msg:
            split=user_msg.split()
            a1=float(split[1])
            print(math.sqrt(a1))
        elif 'log' in user_msg:
            split=user_msg.split()
            a1=float(split[1])
            print(math.log(a1))