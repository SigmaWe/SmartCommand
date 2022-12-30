import os

FOLDER = './MLmodels/'
FILE_NAME = 'cleaned_commands.txt'

def recover_command(FOLDER,FILE_NAME):
    f = open(os.path.join(FOLDER, FILE_NAME),'r')
    original_command = []
    commands = f.readlines()
    commands = [x.replace("\n","") for x in commands]
    for this_command in commands:
        this_command = this_command.replace("_","")
        original_command.append(this_command)
    return original_command
