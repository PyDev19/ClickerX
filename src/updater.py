import os
import subprocess
from urllib.request import urlopen

def check_internet_connection():
    try:
        urlopen('https://www.google.com')
        return True
    except:
        return False

if check_internet_connection():
    print("Internet connection available.")
else:
    print("Internet connection not available.")