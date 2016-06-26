import os
import sys
import logging
from argparse import ArgumentParser

import geojson
import requests

def parse_args(args):
    usage = "Make a map of apartments & condos in Austin with Google Fiber"
    parser = ArgumentParser(usage=usage)

    parser.add_argument(
        "-o",
        "--output",
        dest="out",
        default="atx_fiber_apts.json",
        help="Destination for output geojson"
    )

    parser.add_argument(
        "--url",
        dest="url",
        default="https://www.googleapis.com/storage/v1/b/fiber/o/property-manager%2FAustin1.json",  # noqa
        help="metadata URL"
    )

    parser.add_argument(
        "--overwrite",
        action="store_true",
        default=False,
        help="Specify whether existing output geojson should be overwritten"
    )

    return parser.parse_args(args)


def get_all_locs(metaurl):
    meta = requests.get(metaurl)
    meta = meta.json()
    updated = meta.get("updated", "Unknown date")

    try:
        url = meta["mediaLink"]
    except KeyError:
        return None

    all_locs = requests.get(url)
    return all_locs.json()


def _main(args):
    opts = parse_args(args)

    if os.path.exists(opts.out) and opts.overwrite is False:
        logging.error(
            ("Output already exists: "
             "either specify a new output filename, or use '--overwrite'")
        )
        return 1

    all_current_apts = get_all_locs(opts.url)
    if not all_current_apts:
        return 1
    all_current_apts = get_all_locs()

    ready_apts = []
    for apt in all_current_apts:
        if apt.get("Ready", "").upper() == "TRUE":
            geom = geojson.Point((apt.get("Longitude", 0.0),
                                  apt.get("Latitude", 0.0)))
            ready_apts.append(geojson.Feature(geometry=geom, properties=apt))

    with open("atx_fiber_apts.json", "w") as out:
        out.write(geojson.dumps(geojson.FeatureCollection(ready_apts)))
    return 0


def main():
    sys.exit(_main(sys.argv[1:]) or 0)
