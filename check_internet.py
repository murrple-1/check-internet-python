import sys
import time
import argparse
import urllib.request
import urllib.error


def internet_on(reference_url: str, timeout: float):
    print(f"Trying to connect to '{reference_url}'", file=sys.stderr)
    try:
        request = urllib.request.Request(reference_url, method="HEAD")
        with urllib.request.urlopen(request, timeout=timeout):
            pass
        return True
    except urllib.error.URLError:
        return False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--reference-url", default="http://142.251.41.78")
    parser.add_argument("-t", "--timeout", type=float, default=1)
    parser.add_argument("-s", "--sleep-timeout", type=float, default=5)

    args = parser.parse_args()

    try:
        while not internet_on(args.reference_url, args.timeout):
            print("Internet Down...", file=sys.stderr)
            print("Sleeping for {} seconds".format(args.sleep_timeout), file=sys.stderr)
            time.sleep(args.sleep_timeout)

        print("\a")
        print("Internet back up!", file=sys.stderr)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
