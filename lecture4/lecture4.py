import sys

from lib.log import Log

def count_errors(log):
    """Returns the number of error entries in the log file found at `path`, or
`None` if the file doesn't exist."""

    return len(log.get_errors())


def main():
    if len(sys.argv) != 2:
        print("usage: lecture1 input_file")
        return
    try:
        entries = Log.from_file(sys.argv[1], skip_malformed_entries=True)
        error_count = count_errors(entries)
        print(error_count)
    except FileNotFoundError:
        print("could not open log file")


if __name__ == '__main__':
    main()
