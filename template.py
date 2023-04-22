import os
import sys
from pathlib import Path
import logging

logging.basicConfig(
    level = logging.INFO,
    format="[%(asctime)s: %(levelname)s] %(message)s"
) 

while True:
    project_name = input("Enter your project name:  ")
    if project_name != '':
        break


logging.info(f" creating project by name:  { project_name}")



list_of_files = [

    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/config/__init__.py",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/entiti/__init__.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/utils/__init__.py",
    f"config/config.yaml",
    "setup.py",
    "main.py",
    "requirements.txt",
    "demo.py"
]


for file_path in list_of_files:
    file_path = Path(file_path)
    filedir,filename=os.path.split(file_path)
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"creating new dictonary at: {filedir} for file:{filename}")
    if(not os.path.exists(file_path)) or os.path.getsize (filename==0):
        with open(file_path, "w") as f:
            pass

        logging.info(f"creating new file at: {filedir} for file: {filename}")
else:
        logging.info(f"file already preset  at:  {filename}")












