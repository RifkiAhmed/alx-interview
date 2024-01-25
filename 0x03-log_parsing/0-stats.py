#!/usr/bin/python3
'''Log parsing'''
import re
import sys


count = 0
size = 0
status = {"200": 0, "301": 0, "400": 0, "401": 0,
          "403": 0, "404": 0, "405": 0, "500": 0}
pattern = (
    r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - '
    r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+)\] '
    r'"GET \/projects\/260 HTTP\/1\.1" (.*) (\d+)')


def print_statistics():
    '''Print statistics: total size and number of lines by status code '''
    print(f"File size: {size}")
    for key, value in status.items():
        if value:
            print(f'{key}: {value}')


while True:
    try:
        line = sys.stdin.readline().strip()
        count += 1
        if re.match(pattern, line):
            line_list = line.split()
            size += int(line_list[-1])
            if status.get(line_list[-2]) is not None:
                status[line_list[-2]] += 1
        if line == "":
            print_statistics()
            break
        if count == 10:
            print_statistics()
            count = 0
    except KeyboardInterrupt as err:
        print_statistics()
        raise
