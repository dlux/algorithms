import sys


def main(method):
    pass


if __name__ == '__main__':
    args = sys.argv[1:]
    method = 0 if len(args) == 0 else args[0]
    main(method)
