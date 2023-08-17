import pyautogui
from tkinter import Tk
import tkinter as tk
from jsonc_parser.parser import JsoncParser
import json
import time

pyautogui.PAUSE = 0.5

default_keybindings = JsoncParser.parse_file("default_keybindings.jsonc")

command_title_dic = {}

for keybinding in default_keybindings:
  if keybinding['command'] not in list(command_title_dic.keys()):
    command_title_dic[keybinding['command']] = ''

c_n_b =  open("default_keybindings.jsonc")
for command in c_n_b:
  if command[0:6] == "  // -":
    command_title_dic[command[7:-1]] = ''

# Ctrl-C the test (without single quotes) before running the script
last_command = 'test'
keys_list = list(command_title_dic.keys())
for i in range(len(keys_list)):
  pyautogui.click(x=1000, y=120, clicks=6, button='left')
  pyautogui.typewrite('@command:' + keys_list[i])
  pyautogui.click(x=1000, y=200, clicks=1, button='right')
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

command_title_list = []

for i in range(len(keys_list)):
  print(keys_list[i], ":", command_title_dic[keys_list[i]])
  command_title_list.append({'command_id': keys_list[i], 'command_title': command_title_dic[keys_list[i]]})

with open('command_title_list.json', 'w', encoding='utf-8') as outfile:
  json.dump(command_title_list, outfile, indent=2)