import os
import sys
import json
import logging
from argparse import ArgumentParser

import geojson

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
        "--overwrite",
        action="store_true",
        default=False,
        help="Specify whether existing output geojson should be overwritten"
    )

    return parser.parse_args(args)


def get_all_locs():
    with open("fiber.json") as f:
        apts = json.load(f)
    return apts


def _main(args):
    opts = parse_args(args)

    if os.path.exists(opts.out) and opts.overwrite is False:
        logging.error(
            ("Output already exists: "
             "either specify a new output filename, or use '--overwrite'")
        )
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

def main():
   sys.exit(_main(sys.argv[1:]) or 0)
