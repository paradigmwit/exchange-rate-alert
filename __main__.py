import sys
from ratealert.conversionalert import ConversionAlert


def main(source, target):
    ConversionAlert(source, target)


if __name__ == "__main__":

    if len(sys.argv) != 3:
        print('usage: python3 __main__.py {Source} {Target}'
              'There should be a source and a target currency')
        exit()
    else:
        main(sys.argv[1], sys.argv[2])
