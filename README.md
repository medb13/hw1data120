# DATA120 Assignment 1 – README

Welcome to your first assignment! This assignment will help you review concepts learned during the first week of class.
Each part has its own Python file with directions written directly inside the file.
Please make sure to read and follow the comments in each file carefully.
If you have any additional questions, please reach out on Piazza or attend office hours!

## Files Overview

You’ll be working on the following files:

- 01.py – Printing and Input
- 02.py – Data Types
- 03.py – Operators
- 04.py – Conditionals and Random
- 05.py – ATM Menu Program

All instructions are located inside each file - read them carefully before coding.

There is also an inputs folder provided. Do not modify any files in this folder - they are used for grading and testing your programs.

## How to Open your Terminal

### Mac

Click on the Launchpad icon in your Dock, type “Terminal,” and press Return.

Or, press Command (⌘) + Spacebar to open Spotlight Search, type “Terminal,” and press Return.

The terminal window will open, and you should see a prompt ready for commands.

### Linux
Open your application menu (often accessed by clicking the bottom-left icon or pressing the Super/Windows key) and search for “Terminal.”

Alternatively, use the shortcut Ctrl + Alt + T to open a new terminal window.

Your prompt will usually show your username and machine name.

### Windows (Command Prompt)
Press the Windows key, type cmd for Command Prompt or PowerShell for PowerShell, and press Enter.

Or, press Windows + R, type cmd, and hit Enter to open Command Prompt directly.

Or, right click in the folder in File Explorer and click "Open in Terminal".

A new window will pop up, usually showing something like:

C:\Users\YourName>

## How to Run Your Code

Use the terminal to navigate to the folder where your files are saved. To run a file, use the following command:

```bash
python [file_name.py]
# or
python3 [file_name.py]
```

## Step 1: Generate Your Output File

Before generating a new output.txt file, delete any previous one to avoid mixing old results.

### Mac/Linux
```bash
rm output.txt
```

### Windows (Command Prompt)
```bash
del output.txt
```

Then, in the same directory as your assignment files, run the following commands in order:

### Mac/Linux
```bash
python3 01.py < inputs/input_01.txt > output.txt
python3 02.py >> output.txt
python3 03.py >> output.txt
python3 04.py < inputs/input_04.txt >> output.txt
python3 05.py < inputs/input_05.txt >> output.txt
```

### Windows (Command Prompt)
```bash
python 01.py < inputs\input_01.txt > output.txt
python 02.py >> output.txt
python 03.py >> output.txt
python 04.py < inputs\input_04.txt >> output.txt
python 05.py < inputs\input_05.txt >> output.txt
```

If your system only recognizes python instead of python3, replace python3 with python in all commands above.

## Step 2: Submitting

Verify that your output.txt file contains results for all five parts (01.py through 05.py).

Upload the following files to Gradescope:
- 01.py
- 02.py
- 03.py
- 04.py
- 05.py
- output.txt
- receipt.txt (only if you completed the extra credit)