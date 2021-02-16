from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import requests
import os
import time
import webbrowser

#Before use:
#SignUp in music.apple.com
#Allow remote automations safari

#Verify if music requested was the latest download
while True:
    try:
        with open('musica.txt', 'r') as file:
            musica = file.read()
            print(musica)
            os.remove('musica.txt')
    except:
        musica="0"

    #Request XML

    response = requests.get('https://sulamericaparadiso.com.br/sulamerica.xml')
    #Brazilian Encoding
    response.encoding = 'ISO-8859-1?'

    #Control Time

    import datetime
    now = datetime.datetime.now()
    print("Current date and time : ")
    print(now.strftime("%Y-%m-%d %H:%M:%S"))

    raw=response.text
    print(raw)

    #Get Song Name>'))
    try:
        song = str(raw).split(str('<song>'))
        song=str(song[2])
        song=song.split(str('</song>'))
        song=song[0]
        print(song)

        #Verify if file exists, if yes end.
        if musica == str(song):
            file = open("musica.txt", "w")
            file.write(song)
            file.close()
            time.sleep(30)
        else:

            #Get artist Name
            singer=str(raw).split(str('<singer>'))
            singer=str(singer[1])
            singer=singer.split(str('</singer>'))
            singer=singer[0]

            #Avoid get Banner

            if song == "SulAm?rica Paradiso FM" or singer == "Nossa mistura ? diferente":
                print("do nothing")
            else:
                #Create control music file
                file = open("musica.txt", "w")
                file.write(song)
                file.close()
                #song="a-ha"
                #singer="take on me"
                print(singer)
                path="https://music.apple.com/cz/search?term="+song+" "+singer
                print(path)
                webbrowser.open(path, new=2)
                #driver = webdriver.Safari()
                #driver.get(path)
                #driver.maximize_window()
                time.sleep(50)
                #pyautogui.move(-0770, 220)
                pyautogui.click(560, 290, button='left')
                time.sleep(5)
                pyautogui.click(590, 290, button='left')
                time.sleep(5)
                pyautogui.click(750, 340, button='left')
                time.sleep(10)
                os.system('osascript -e "tell application \\"Safari\\" to quit"')
                time.sleep(60)

    except:
        print("error")
        pass