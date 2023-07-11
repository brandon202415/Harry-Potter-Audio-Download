# Potterdownload
potterdownload downloads all chapters of the 7 Harry Potter audiobooks, narrated by Jim Dale, and sorts them into folders.
# Installation
Several modules are required to run the Python code (assumed to be Python 3).
To download:
```
pip3 install pathlib
pip3 install requests
pip3 install bs4
```
Once the required modules are downloaded,
```
git clone https://github.com/brandon202415/potterdownload.git
```
# Usage
Navigate into the cloned directory
```
cd potterdownload
```
Once in the correct directory, run the command
```
python3 potterdownload.py
```
The program will create 7 folders (inside the current directory) and begin downloading the Harry Potter audiobooks.

Note: This is very large (1.3 GB) download, so expect it to take several minutes depending on download speed.
