print("Hello world")

import pyautogui
pyautogui.moveTo(650, 1050)  # met deze comand beweeg hij mijn muis naar de ingevoerde coördinaten
pyautogui.click(650, 1050) # en hier klikt hij met mijn muis op de ingevorde coördinaten
pyautogui.moveTo(700, 900) # hier beweeg hij naar de bepaalde folder
pyautogui.click(700, 900) # nu selecteert hij de folder
pyautogui.moveTo(600, 450) # dit is waar hij naar the png gaat
pyautogui.dragTo(500, 450, 2) # uiteindelijk beweeg hij de png naar de folder