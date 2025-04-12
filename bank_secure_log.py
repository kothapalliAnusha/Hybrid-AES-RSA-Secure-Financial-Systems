# bank_secure_log.py
import logging
import os

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/bank_log.log",
    filemode='a',
    format='%(asctime)s | %(levelname)s | %(message)s',
    level=logging.INFO
)

def log_event(event_type, message):
    event_type = event_type.lower()
    if event_type == "info":
        logging.info(message)
    elif event_type == "error":
        logging.error(message)
    elif event_type == "warning":
        logging.warning(message)
    else:
        logging.debug(message)
