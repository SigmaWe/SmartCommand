import re

with open('raw_commands.txt') as f:
    lines = f.read()
f.close()

regex = "(\"command\": \")([\S\s]*)(\",\n)"
compiled_regex = re.compile(regex,re.MULTILINE)
commands = re.findall(compiled_regex, lines)
print(commands[0])