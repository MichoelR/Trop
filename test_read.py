import os
from bs4 import BeautifulSoup

with open("Books/Genesis.xml") as file: 
    soup = BeautifulSoup(file.read())
    print(list(soup.strings)[200:250])


