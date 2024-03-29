#!/usr/bin/python3
""" module for log parsing"""
import sys
import datetime


status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
total_size = 0
counter = 0

try:
    log_lines = sys.stdin
    for line in log_lines:
        line_l = line.split(" ")
        if len(line_l) >= 5 and len(line_l[0].split(".")) == 4 \
                and len(line_l[2].split("-")) == 3 and line_l[4] == '"GET' \
                and line_l[7] in str(status_codes.keys()) \
                and int(line_l[8]) in range(1, 1024):
            if len(line_l[-2]) == 3:
                status = int(line_l[-2])
            size = int(line_l[-1])
            if status in status_codes.keys():
                status_codes[status] += 1
                total_size += size
                counter += 1
            if counter == 10:
                print("File size: {}".format(total_size))
                for key, value in sorted(status_codes.items()):
                    if value != 0:
                        print("{}: {}".format(key, value))
                counter = 0

except Exception:
    pass

finally:
    print("File size: {}".format(total_size))
    for key, value in sorted(status_codes.items()):
        if value != 0:
            print("{}: {}".format(key, value))
    counter = 0
