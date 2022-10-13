# Text2Command by sentenceBERT

This folder aims to achieve the text to command using the EMNLP2019 paper [sentenceBERT](https://arxiv.org/abs/1908.10084). I will use the associated implemented package [SentenceTransformers](https://www.sbert.net/).

I also borrow a lot of code from [Dr. Bao's NLP class](https://github.com/forrestbao/pebble/blob/master/NLP/semantic_search.ipynb)

# Sample text commands:

The VS Code Palette has the associated built-in commands but will not return correct built-in commands if using the following sample natural language search. The left is the natural language command and the right is the correct built-in commands.

1. `preview markdown file` <> `show preview`;
2. `open another VS code` <> `new window`;
3. `create an empty file` <> `new file`;
4. `close all windows` <> `close window`;

# Result:
```
Current command:preview markdown file
change to markdown----------------------  66.02% match
show preview----------------------------  63.79% match
preview declaration---------------------  60.80% match
preview---------------------------------  60.46% match
open preview----------------------------  56.66% match
--------------------------------------------------------------------------------
Current command:open another VS code
open on vscode dev----------------------  64.82% match
open file-------------------------------  54.35% match
open file-------------------------------  54.35% match
open in editor--------------------------  54.18% match
open snippets---------------------------  51.82% match
--------------------------------------------------------------------------------
Current command:create an empty file
new file--------------------------------  61.74% match
new file--------------------------------  61.74% match
create file from explorer---------------  56.97% match
create empty profile--------------------  54.90% match
delete file-----------------------------  50.61% match
--------------------------------------------------------------------------------
Current command:close all windows
close window----------------------------  80.54% match
close panel-----------------------------  61.89% match
close all-------------------------------  61.72% match
close folder----------------------------  60.86% match
close all groups------------------------  58.37% match
--------------------------------------------------------------------------------
```

# Insights

The command could be vague. For example `close all windows` could mean to close all editors.