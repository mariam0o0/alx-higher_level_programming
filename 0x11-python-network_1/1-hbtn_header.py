#!/usr/bin/python3
"""Displays  the X-Request-Id variable found in the header of the response."""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    link = urllib.request.Request(url)
    with urllib.request.urlopen(link) as response:
        print(dict(response.headers).get("X-Request-Id"))
