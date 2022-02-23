import time
import datetime
import os
import sys


for i in range(1, 4):
    print(f"{i}...")
    time.sleep(1)

print(datetime.datetime.now().microsecond)
print(os.name)
print(sys.argv)
