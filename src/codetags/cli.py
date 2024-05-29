#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  cli.py
#
#  Copyright 2022 Marco Ramos <majramos@gmail.com>
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
from .codetags import CodeTags, TAGS




def validate_tag(value: str) -> str:
    """ Validate if the input tag is a valid one """
    if value in TAGS:
        return value
    else:
        raise argparse.ArgumentTypeError(f"'{value}' is not a valid tag")
        
        
def validate_loc(value: str) -> Path:
    """ Validate if the location/file exists. The location has base CWD """
    loc = Path()/value
    if loc.exists():
        return loc
    else:
        raise argparse.ArgumentTypeError(f"'{loc}' is not a location")


def operations(args: CodeTags):

    # files = get_files()
    # findings = list_tags(search_files(files))
    # print_findings(findings)
   
    
    if args.output is None:
        args.output = 'codetags.txt'

    print(args)


def main() -> None:
    """ Main execution """

    parser = argparse.ArgumentParser(prog='codetags',
                                     allow_abbrev=False,
                                     description='Locate tags in code files')
                                     
    parser.add_argument('-l', '--loc',
                        default=Path(),
                        type=validate_loc,
                        metavar='path',
                        help='path where to search files (defaults to current working directory)')

    parser.add_argument('-o', '--output',
                        default=False, #'codetags.txt',
                        metavar='file',
                        nargs='?',
                        help='output findings to file (defaults to codetags.txt)')
                        
    parser.add_argument('-s', '--sort',
                        help='hot to sort the findings')
                        
    parser.add_argument('-t', '--tag',
                        default=TAGS,
                        type=validate_tag,
                        nargs='+',
                        help='tags to search: BUG,FIXME,NOTE,TODO (defaults to all)')

    parser.add_argument('-v', '--version',
                        action='version',
                        version=f'%(prog)s {__version__}',
                        help='display package version')

    ct = CodeTags()
    operations(parser.parse_args(namespace=ct))


if __name__ == "__main__":
    main()
