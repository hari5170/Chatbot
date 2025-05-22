import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s] %(levelname)s: %(message)s')

list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "research/trails.ipynb",
    "test.py"]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename= os.path.split(filepath)

    if filedir:
        logging.info(f"Creating directory: {filedir} for file :{filename}")
        os.makedirs(filedir, exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)) == 0:
        with open(filepath, 'w') as f:
            pass    
            logging.info(f"Creating file: {filepath}")
       
    else:
        logging.info(f"File already exists: {filename}")

