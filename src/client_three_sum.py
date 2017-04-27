from three_sum import THREESUM
import sys


def main():
    # Compute a list of numbers or read from a file and pass the list to compute
    my_args = sys.argv[1:]
    sums = THREESUM()

    if not my_args:
        my_args = [sums.generate_file()]

    if len(my_args) == 1:
        my_args = sums.read_file(my_args[0])

    count =sums.count(my_args)
    print("Three sums with zero result: {0}".format(count))


if __name__ == "__main__":
    main()

