#!/usr/bin/env python

from datetime import datetime
from pathlib import Path
import time
import sys

def has_hidden_parent(path):
    return any(file.name.startswith('.') for file in path.parents)

def get_latest_ctime():
    return max(
            file.stat().st_ctime
            for file in Path('.').glob('**/*')
            if not has_hidden_parent(file)
    )

if __name__ == '__main__':
    wait_time = float(sys.argv[1]) if len(sys.argv) > 1 else 1
    current = get_latest_ctime()
    print(f'Current latest update {datetime.fromtimestamp(current)}')
    print(f'Waiting for change every {wait_time}s')
    while current == (new := get_latest_ctime()):
        time.sleep(wait_time)
    print(f'New latest update detected: {datetime.fromtimestamp(new)}')
