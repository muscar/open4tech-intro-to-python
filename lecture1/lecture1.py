import sys
import os

def count_errors(path):
    """Returns the number of error entries in the log file found at `path`, or
`None` if the file doesn't exist."""

    if not os.path.isfile(sys.argv[1]):
        return
    error_count = 0
    with open(path, 'r') as input_file:
        for line in input_file:
            if line.startswith("ERROR"):
                error_count += 1
    return error_count


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
