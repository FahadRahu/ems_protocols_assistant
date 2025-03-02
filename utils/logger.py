import logging

logging.basicConfig(level=logging.INFO, filename='log.txt', format='%(asctime)s - %(message)s')

def log_event(event):
    logging.info(event)
