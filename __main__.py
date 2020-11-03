import sys
from ratealert import ConversionAlert


def main(source, target, alert_rate):
    ConversionAlert(source, target, alert_rate)


if __name__ == "__main__":

    if len(sys.argv) != 4:
        print('usage: python3 __main__.py {Source} {Target} {Target}. \n'
              'There should be a source, target currency and target rate for checking the api.')
        exit()
    else:
        main(sys.argv[1], sys.argv[2], sys.argv[3])
