import pyautogui
from tkinter import Tk
import tkinter as tk
import json
import time

pyautogui.PAUSE = 0.5

with open("default_keybindings.json") as d_k:
  default_keybindings = json.load(d_k)

command_title_dic = {}

for keybinding in default_keybindings:
  if keybinding['command'] not in list(command_title_dic.keys()):
    command_title_dic[keybinding['command']] = ''

c_n_b =  open("commands_not_bound.txt")
for command in c_n_b:
  command_title_dic[command[5:-1]] = ''

# Ctrl-C the test (without single quotes) before running the script
last_command = 'test'
keys_list = list(command_title_dic.keys())
for i in range(len(keys_list)):
  pyautogui.click(x=1000, y=120, clicks=6, button='left')
  pyautogui.typewrite('@command:' + keys_list[i])
  pyautogui.click(x=1000, y=200, clicks=1, button='right')
  # pyautogui.moveTo(x=1200, y=295)
  # time.sleep(2)
  pyautogui.click(x=1200, y=295, clicks=1, button='left')
  try:
    new_command = Tk().clipboard_get()
    if new_command == last_command:
      command_title_dic[keys_list[i]] = ''
    else:
      command_title_dic[keys_list[i]] = new_command
    last_command = new_command
  except tk.TclError:
    print("tk error")
    break
  # if i > 55:
  #   break

command_title_list = []

for i in range(len(keys_list)):
  print(keys_list[i], ":", command_title_dic[keys_list[i]])
  command_title_list.append({'command_id': keys_list[i], 'command_title': command_title_dic[keys_list[i]]})

with open('command_title_list.json', 'w', encoding='utf-8') as outfile:
  json.dump(command_title_list, outfile, indent=2)

# command_list = []

# while True:
# pyautogui.hotkey('ctrl', 'shift', 'p')
# pyautogui.moveTo(x=1300, y=80)
# pyautogui.click(x=1300, y=110, clicks=3, button='left')
# pyautogui.hotkey('ctrl', 'c')
# command_list.append(Tk().clipboard_get())
# print(Tk().clipboard_get())
# pyautogui.hotkey('ctrl', 'shift', 'p')
# pyautogui.moveTo(x=1300, y=80)
# pyautogui.scroll(-50)

# import pyautogui, sys
# print('Press Ctrl-C to quit.')
# try:
#     while True:
#         x, y = pyautogui.position()
#         positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#         print(positionStr, end='')
#         print('\b' * len(positionStr), end='', flush=True)
# except KeyboardInterrupt:
#     print('\n')