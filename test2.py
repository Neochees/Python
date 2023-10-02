import pyautogui

pyautogui.write('Watch this :3', interval = 0.1) # hier typed hij wat text
pyautogui.hotkey('alt', 'tab') # nu veranderd hij van tabblad
pyautogui.hotkey('ctrl', 't') # dan voegt hij hier een nieuw tabblad aan
pyautogui.write('https://www.youtube.com/watch?v=dQw4w9WgXcQ', interval = 0) # en plaats hij de link
pyautogui.hotkey('enter') # uiteindelijk zoekt hij de geplaatste link op

