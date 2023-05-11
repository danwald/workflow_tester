import logging
import os


MSG_SSID = os.getenv('MSSID', 'foobar')
SID = os.getenv('SID', 'foobar')
LOG_LEVEL = logging.DEBUG

logging.basicConfig(level=LOG_LEVEL, format='%(asctime)s - %(levelname)s - %(message)s')
