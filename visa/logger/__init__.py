from datetime import datetime
import logging
import os, sys

LOG_DIR = "logs"

CURRENT_TIME_STEMP = f"{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}"

# YEAR, MONTH, DAY, HOURS, MINUTUE,SEC

log_file_name = f"logs{CURRENT_TIME_STEMP}.log"

os.makedirs(LOG_DIR,exist_ok=True)

log_file_psth = os.path.join(LOG_DIR, log_file_name)

logging.basicConfig(filename =log_file_psth, 
                    filemode="w" ,
                    format='[%(asctime)s], %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO
                    )
