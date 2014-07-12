import sys
import os

from datetime import datetime as dt


ENTRY_INFO = 0
ENTRY_WARNING = 1
ENTRY_ERROR = 2

# (TAG, DATE, MSG)

def get_entry_kind(entry):
    """Rerturns the tag for a given entry."""

    if entry.startswith('INFO'):
        return ENTRY_INFO
    if entry.startswith('WARNING'):
        return ENTRY_WARNING
    if entry.startswith('ERROR'):
        return ENTRY_ERROR


def parse_log_entry(line):
    """Returns a log entry from a log line."""
    
    components = line.split(' ', maxsplit=2)
    entry_date = dt.strptime(components[1], '%Y-%m-%d')
    return (components[0], entry_date, components[2])


def read_log(path):
    if not os.path.isfile(path):
        return
    entries = []
    with open(path, 'r') as input_file:
        for line in input_file:
            entries.append(parse_log_entry(line))
        return entries


def count_errors(path):
    """Returns the number of error entries in the log file found at `path`, or
`None` if the file doesn't exist."""

    if not os.path.isfile(path):
        return
    with open(path, 'r') as input_file:
        return len([line for line in input_file if get_entry_kind(line) == ENTRY_ERROR])


def main():
    if len(sys.argv) != 2:
        print("usage: lecture1 input_file")
        return
    error_count = count_errors(sys.argv[1])
    if error_count is None:
        print("oops, boo boo! does the file exist?")
    else:
        print(error_count)


if __name__ == '__main__':
    main()
