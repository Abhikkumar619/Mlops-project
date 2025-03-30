import logging
import os
from datetime import datetime
import sys


format_str = "[%(asctime)s : %(levelname)s : %(module)s : %(message)s]"

Logdir="Log"
os.makedirs(Logdir, exist_ok=True)

file_name=f"{datetime.now().strftime('%m_%d_%Y_%H_%S')}.log"
file_path=os.path.join(Logdir, file_name)


logging.basicConfig(level=logging.DEBUG, 
                    format=format_str,
                    handlers=[logging.StreamHandler(sys.stdout),
                              logging.FileHandler(file_path)
                               ])
log=logging.getLogger("mlops_project")
