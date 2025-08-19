#!/usr/bin/python3

import argparse
import urllib.request

FILES = [
    "a2dp-codec-aac.c",
    "a2dp-codec-caps.h",
    "bap-codec-caps.h",
    "media-codecs.c",
    "media-codecs.h",
    "rtp.h",
]

URL_PATTERN = "https://gitlab.freedesktop.org/pipewire/pipewire/-/raw/{tag}/spa/plugins/bluez5/{file}"


def update(tag: str) -> None:
    for file in FILES:
        url = URL_PATTERN.format(tag=tag, file=file)
        urllib.request.urlretrieve(url, file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("tag")
    args = parser.parse_args()
    update(args.tag)
