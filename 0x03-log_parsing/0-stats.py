#!/usr/bin/python3
"""compute metrics"""


if __name__ == "__main__":
    import sys

    status_codes = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
    }
    total_size = 0
    counter = 0

    try:
        for i, line in enumerate(sys.stdin, 1):
            data = line.split()
            if len(data) > 2:
                size = data[-1]
                code = data[-2]
                total_size += int(size)
                if code in status_codes:
                    status_codes[code] += 1
            if i % 10 == 0:
                print("File size: {}".format(total_size))
                for k, v in sorted(status_codes.items()):
                    if v != 0:
                        print("{}: {}".format(k, v))
    except KeyboardInterrupt:
        pass
    finally:
        print("File size: {}".format(total_size))
        for k, v in sorted(status_codes.items()):
            if v != 0:
                print("{}: {}".format(k, v))
