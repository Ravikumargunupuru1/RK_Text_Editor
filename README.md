# RK Text Editor
**RK Text Editor** is a simple and user-friendly text editor built using Python's Tkinter library. It allows users to open, edit, and save text files with ease. The project includes a modern GUI design with dynamic buttons that change color when hovered over, enhancing the user experience.

# Features
* Open text files for editing.
* Save As functionality to save changes or create new text files.
* Dynamic UI with sliding color buttons for improved interactivity.
* Resizable text area for convenient editing.
* Undo/Redo functionality for text manipulation.

# Requirements
* Python 3.x (Preferably 3.6 or higher)
* Tkinter (Usually included with Python)
* PyInstaller (For packaging the app into an executable)

# Installing Dependencies
To install the necessary dependencies:
* Install Python 3.x from [python.org](https://www.python.org/downloads/).
* Tkinter comes pre-installed with most Python distributions. However, on Linux, you may need to install it:
```bash
sudo apt-get install python3-tk
```
* Install PyInstaller (optional, for creating an executable):
```bash
pip install pyinstaller
```

# Usage
1. Running the Editor
* To run RK Text Editor, simply execute the following command:
```bash
python text_editor.py
```
* This will launch the text editor GUI.

2. Creating an Executable
* If you want to distribute the text editor as a standalone executable:
```bash
pyinstaller --onefile --noconsole text_editor.py
```
The executable will be available in the dist folder created by PyInstaller.
