#!/usr/bin/python3
""" log parsing """
import sys
import re


def initialiseLog():
    """initialise the log"""
    status_codes = [200, 301, 400, 401, 403, 404, 405, 500]

    log = {"file_size": 0, "codes": {str(code): 0 for code in status_codes}}

    return log


def parse(str, regex, log):
    """parse the standard input and returns the final log"""
    match = regex.fullmatch(str)

    if match:
        status_code, fileSize = match.group(1, 2)
        log["file_size"] += int(fileSize)

        if status_code.isdecimal():
            log["codes"][status_code] += 1

    return log


def printOutput(log):
    """prints the final output"""
    print("File size: {}".format(log["file_size"]))
    for code in sorted(log["codes"]):
        if log["codes"][code]:
            print("{}: {}".format(code, log["codes"][code]))


def main():
    """main function"""
    regex = re.compile(
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+\] "GET /projects/260 HTTP/1.1" (.{3}) (\d+)')  # nopep8

    log = initialiseLog()
    count = 0

    for line in sys.stdin:
        line = line.strip()
        count += 1

        log_after_parse = parse(line, regex, log)

        if count % 10 == 0:
            printOutput(log_after_parse)


if __name__ == "__main__":
    main()
