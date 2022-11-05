import greet as g
q=["quit","q"]
quit_msg=["Thanks for using,Bye","Let's meet again,Bye","Bubye","See you again","I'm here if you need my help again"]
greetings=g.greet()
print(greetings,",","Have a good day!. I am a WORDBOT.I'm here to help you with some english words you need meaning for:). Start by entering your word")

while True:
    user_msg= input()
    if user_msg in q:
        n=r.randint(0,len(quit_msg))
        print(quit_msg[n])
    else: