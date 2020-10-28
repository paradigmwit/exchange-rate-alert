import sys
from ratealert.conversionalert import ConversionAlert


def main(source, target, interval):
    ConversionAlert(source, target, interval)


if __name__ == "__main__":

    if len(sys.argv) != 4:
        print('usage: python3 __main__.py {Source} {Target} {Interval}. \n'
              'There should be a source, target currency and interval for checking the api.')
        exit()
    else:
        main(sys.argv[1], sys.argv[2], sys.argv[3])
