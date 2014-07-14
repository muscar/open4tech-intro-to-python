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
    entries = Log.from_file(sys.argv[1])
    error_count = count_errors(entries)
    if error_count is None:
        print("oops, boo boo! does the file exist?")
    else:
        print(error_count)


if __name__ == '__main__':
    main()
