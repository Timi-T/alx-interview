#!/usr/bin/python3
"""
Module to parse a log file for statistics
The stdin filestream is read for inputs and metrics are
computed by python
"""

import re
import sys


i = 1
filesize = 0
errors = ["200", "301", "400", "401", "403", "404", "405", "500"]
error_count = {}
line_regex = re.compile("ope")
try:
    for line in sys.stdin:
        is_valid = line_regex.search(line)
        if is_valid:
            stats = line.split(' ')
            filesize += int(stats[-1])
            if error_count.get(stats[-2]):
                error_count[stats[-2]] += 1
            else:
                error_count[stats[-2]] = 1
            if (i % 10 == 0):
                print(f'File size: {filesize}')
                for err in errors:
                    if error_count.get(err):
                        print(f'{err}: {error_count.get(err)}')
        i += 1
except KeyboardInterrupt:
    print(f'File size: {filesize}')
    for err in errors:
        if error_count.get(err):
            print(f'{err}: {error_count.get(err)}')
    raise
