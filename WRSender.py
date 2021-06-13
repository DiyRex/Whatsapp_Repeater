import pyautogui
import time

name = """  

 _   _ _____ ___  __  ___    __  ___ __  _ __  ___ ___  
| | | |_   _|_  |/  \| _,\ /' _/| __|  \| | _\| __| _ \ 
| 'V' | | |  / /| /\ | v_/ `._`.| _|| | ' | v | _|| v / 
!_/ \_! |_| |___|_||_|_|   |___/|___|_|\__|__/|___|_|_\ 
                                                                                              
                           Script By -DiyRex- :)
"""


print(name, "\n")




time.sleep(5)
wrd = input("Enter Msg:")
num = int(input("No. Of Msg:"))
print("enter delay 0S or 5S")
T=int(input("Enter Delay:"))
print("click on whatsapp typing bar and wait :)")
time.sleep(5)

for n in range(num):
  pyautogui.typewrite(wrd)
  time.sleep(T)
  pyautogui.press("Enter")

print("...................")
print("Sent Successful!!")

