#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  cli.py
#
#  Copyright 2022 Marco Ramos <code@marcoramos.me>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#


"""
Module for the cli part of the package
"""

import argparse
from pathlib import Path

from codetags import __version__
from .utils import TAGS


def validate_loc(path: str) -> Path:
    """ Validate if the location/file exists. The location has base CWD """

    loc = Path(path).resolve()
    if loc.exists():
        return loc
    else:
        raise argparse.ArgumentTypeError(f"'{loc}' is not a location")


def main() -> None:
    """ Main execution """

    parser = argparse.ArgumentParser(
        prog="codetags",
        allow_abbrev=False,
        description="Locate tags in code files",
        epilog="Thanks for using %(prog)s!"
    )

    parser.add_argument(
        "-l", "--loc",
        default=Path().resolve(),
        type=validate_loc,
        metavar="path",
        help="path where to search .py files (defaults to ./)"
    )

    parser.add_argument(
        "-o", "--output",
        default=".",
        type=validate_loc,
        metavar="file",
        nargs="?",
        help="output location of findings file (defaults to ./codetags.txt)"
    )

    parser.add_argument(
        "-s", "--sort",
        default=False,
        action="store_true",
        help="how to sort the findings"
    )

    parser.add_argument(
        "-t", "--tag",
        choices=TAGS,
        default=TAGS,
        nargs="+",
        help="tags to search (defaults to all)"
    )

    parser.add_argument(
        "-v", "--version",
        action="version",
        version=f"%(prog)s {__version__}",
        help="display package version"
    )

    # ct = CodeTags()
    print(parser.parse_args())


if __name__ == "__main__":
    main()
