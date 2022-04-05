import ctypes
from ctypes import wintypes
import psutil

from pynput.keyboard import Key, Controller

import random
import os
import sys
import keyboard  # using module keyboard
from threading import Timer
from playsound import playsound
from vinanti import Vinanti #easier and simpler async code 
vnt = Vinanti(block=False)

nopes = [
    'F:\\soundpad\\no\\oof.wav',
    'F:\\soundpad\\no\\epic.wav',
    'F:\\soundpad\\no\\failure.wav',
    'F:\\soundpad\\no\\michael.wav',
    'F:\\soundpad\\no\\nope.wav',
    'F:\\soundpad\\no\\vader.wav',
    'F:\\soundpad\\no\\yoda.wav',
    'F:\\soundpad\\no\\what.wav',
]

powers = [
    'F:\\soundpad\\r2.wav',
    'F:\\soundpad\\boosto.wav',
    'F:\\soundpad\\mowpowa.wav'
]

nopes_len = len(nopes)
powers_len = len(powers)
global prev_r

prev_r = 9999
prev_p = 9999

global profile
profile = 0

# keyboarda = Controller()

# from pynput.mouse import Button, Controller

# mouse = Controller()


print('hello')

def check_window():
    global profile
    user32 = ctypes.windll.user32
    h_wnd = user32.GetForegroundWindow()
    pid = wintypes.DWORD()
    user32.GetWindowThreadProcessId(h_wnd, ctypes.byref(pid))
    exe = psutil.Process(pid.value).name()
    print(exe)
    if (exe == 'Adobe Premiere Pro.exe'):
        profile = 1

    print(profile)
def request(url):    
    f = vnt.get(url)

def mainscene():
    print('main')
    request('http://192.168.100.91:1880/scene/main')

def filter1():
    keyboard.press_and_release('ctrl+f1')

def f13():
    # print('f13')
    request('http://192.168.100.91:1880/peter')

def f14():
    # print('f14')
    global prev_r 
    r = random.randint(0, (nopes_len-1))    
    request('http://192.168.100.91:1880/counter1/add')
    request('http://192.168.100.91:1880/lights/police')   
    request('http://192.168.100.91:1880/highlight/oof')   

    request('http://192.168.100.91:1880/scene/zoom')                      
    zoomt = Timer(1.5, mainscene)
    zoomt.start()           

    while prev_r == r:
        r = random.randint(0, (nopes_len-1))   
    playsound(r''+nopes[r], False)
    filter1()
    timer = Timer(1.5, filter1)
    timer.start()
def f15():
    # print('f15')
    global prev_r  
    r = random.randint(0, (nopes_len-1))    
    request('http://192.168.100.91:1880/counter2/add')
    request('http://192.168.100.91:1880/scene/zoom')                      
    # request('http://192.168.100.91:1880/highlight/oof')   
    zoomt = Timer(1.5, mainscene)
    zoomt.start()                          
    
    while prev_r == r:
        r = random.randint(0, (nopes_len-1))                            
    playsound(r''+nopes[r], False)
    prev_r = r

    keyboard.press_and_release('ctrl+f2')
    timer = Timer(1.5, lambda: keyboard.press_and_release('ctrl+f2'))
    timer.start()

def f16():
    # print('f16')
    timer = Timer(1.4, lambda: playsound(r'F:\\soundpad\\drinking.wav', False))
    timer.start()

def f17():
    # print("f17")
    global prev_p       
    p = random.randint(0, (powers_len-1))
    print(prev_p)         
    print(p)
    while prev_p == p:            
        p = random.randint(0, (powers_len-1))       
    print(p)                     
    playsound(r''+powers[p], False) 
    prev_p = p

    request('http://192.168.100.91:1880/scene/zoom')                      
    zoomt = Timer(1.5, mainscene)
    zoomt.start()          

    keyboard.press_and_release('ctrl+f3')
    timer = Timer(1.5, lambda: keyboard.press_and_release('ctrl+f3'))
    timer.start()

def f18():
    # print("f18")
    check_window()
    print(profile)
    # keyboard.press_and_release('=')
    keyboarda.press('=')
    # if(profile == 1):
    #     print('=')
    # else:
    os.system('nircmd changeappvolume chrome.exe -0.01')            
    os.system('nircmd changeappvolume Music.UI.exe -0.01') 

def f19():
    # print("f19")
    # keyboarda.press('-')
    # check_window()
    # keyboard.press_and_release('ctrl+shift+-')
    # if(profile == 1):
    # else:
    os.system('nircmd changeappvolume chrome.exe +0.01')                
    os.system('nircmd changeappvolume Music.UI.exe +0.01') 

def f20():
    # print("f20")
    request('http://192.168.100.91:1880/mustang')
    request('http://192.168.100.91:1880/highlight/mustang')

def f21():
    # print("f21")
    # mouse.scroll(0, 2)
    os.system('nircmd changeappvolume focused -0.05')

def sf21():    
    os.system('nircmd changeappvolume discord.exe -0.05')

def f22():
    # print("f22")
    # mouse.scroll(0, -2)
    os.system('nircmd changeappvolume focused +0.05') 

def sf22():
    os.system('nircmd changeappvolume discord.exe +0.05')    

def f23():
    # print("f23")
    playsound(r'F:\\soundpad\\stuck.wav', False)     

    request('http://192.168.100.91:1880/scene/zoom')                      
    zoomt = Timer(1.5, mainscene)
    zoomt.start()          

    keyboard.press_and_release('ctrl+f2')
    timer = Timer(1.5, lambda: keyboard.press_and_release('ctrl+f2'))
    timer.start()
def f24():
    # print("f24")
    playsound(r'F:\\soundpad\\subuwu.wav', False)   
    request('http://192.168.100.91:1880/ssubuwu')
    request('http://192.168.100.91:1880/highlight/subuwu')  

def f2():
    print('f2')

def f3():
    print('f3')

def f4():
    print('f4')

def f5():
    print('f5')

# keyboard.wait()
keyboard.add_hotkey('f13', f13)
keyboard.add_hotkey('f14', f14)
keyboard.add_hotkey('f15', f15)
keyboard.add_hotkey('f16', f16)
keyboard.add_hotkey('f17', f17)
keyboard.add_hotkey('f18', f18)
keyboard.add_hotkey('f19', f19)

keyboard.add_hotkey('f20', f20)
keyboard.add_hotkey('f21', f21)
keyboard.add_hotkey('shift+f21', sf21)
keyboard.add_hotkey('f22', f22)
keyboard.add_hotkey('shift+f22', sf22)
keyboard.add_hotkey('f23', f23)
keyboard.add_hotkey('f24', f24)
keyboard.add_hotkey('ctrl+alt+f2', f2)
keyboard.add_hotkey('ctrl+alt+f3', f3)
keyboard.add_hotkey('ctrl+alt+f4', f4)
keyboard.add_hotkey('ctrl+alt+f5', f5)

while True:
    event = keyboard.read_event()
    print(event.name)
    

# keyboard.add_hotkey('ctrl+alt+p', lambda: print('alt p yo!'))