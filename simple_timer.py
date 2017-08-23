import time
from datetime import datetime

while True:
    now = datetime.now()
    print(datetime.strftime(now, '%m/%d/%Y %H:%M:%S'), end='', flush=True)
    time.sleep(1)
    print('\r', end='', flush=True)