#!/usr/bin/python3
'''Log parsing'''
import re
import sys


count = 0
size = 0
status = {"200": 0, "301": 0, "400": 0, "401": 0,
          "403": 0, "404": 0, "405": 0, "500": 0}
pattern = re.compile(
    r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - '
    r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+)\] '
    r'"GET \/projects\/260 HTTP\/1\.1" (.*) (\d+)')


def print_statistics():
    '''Print statistics: total size and number of lines by status code '''
    print(f"File size: {size}")
    for key, value in status.items():
        if value:
            print(f'{key}: {value}')


try:
    for line in sys.stdin:
        count += 1
        if re.match(pattern, line):
            line_parts = line.split()
            size += int(line_parts[-1])
            if line_parts[-2] in status:
                status[line_parts[-2]] += 1
        if not line:
            print_statistics()
            break
        if count == 10:
            print_statistics()
            count = 0
    print_statistics()
except KeyboardInterrupt:
    print_statistics()
    raise KeyboardInterrupt