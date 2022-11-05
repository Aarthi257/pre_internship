import random as r
def greet():
    greetings=["Hi","Hello","Hola","Vanakkam","Namaste","Yo!"]
    n=r.randint(0,len(greetings))
    return(greetings[n])
