import threading

def infinite_loop():
    while 1==1:
        pass

def myname():
    print("My Name Is Abin")

# infinite_loop()
# myname()
# It wount show anything
# But if we create thread it can run multiple task at the same time

t1= threading.Thread(target=infinite_loop)
t2=threading.Thread(target=myname)

t1.start()
t2.start()