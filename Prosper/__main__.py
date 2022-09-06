from GUI import GUI
GUI()

from glob import glob
from os import remove, removedirs, getcwd
print("\nCommencing PyCache Clean Up")
project_path = getcwd()
py_cache_files = glob(project_path + "\\**\\*.pyc", recursive=True)
py_cache_folders = glob(project_path + "\\**\\__pycache__", recursive=True)
for file in py_cache_files:
    try:
        remove(file)
    except FileNotFoundError:
        print("Error removing .pyc files.")
for directory in py_cache_folders:
    try:
        removedirs(directory)
    except FileNotFoundError:
        print("Error removing _pycache__ directories.")