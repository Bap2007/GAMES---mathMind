import sys
import os

def get_resource_path(relative_path):
    # if the script is executed with Pyinstaller
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    # either, return the absolute path
    return os.path.join(os.path.abspath("."), relative_path)