import sys
import time
import argparse

import requests


def internet_on(reference, timeout):
    print('Trying to connect to \'{}\''.format(reference), file=sys.stderr)
    try:
        requests.head(reference, timeout=timeout)
        return True
    except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
        return False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-r',
        '--reference-url',
        default='http://216.58.192.142')
    parser.add_argument('-t', '--timeout', type=float, default=1)
    parser.add_argument('-s', '--sleep-timeout', type=float, default=5)

    args = parser.parse_args()

    while not internet_on(args.reference_url, args.timeout):
        print('Internet Down...', file=sys.stderr)
        print(
            'Sleeping for {} seconds'.format(
                args.sleep_timeout),
            file=sys.stderr)
        time.sleep(args.sleep_timeout)

    print('\a')
    print('Internet back up!', file=sys.stderr)


if __name__ == '__main__':
    main()
