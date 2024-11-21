#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  codetags.py
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


"""
module to search for target files and search for comments with tags
"""


import re
from pathlib import Path
# from operator import itemgetter
from typing import Iterator, Optional

from .utils import ParsedTags, select_tags


# regular expressions
RE_P = re.compile(r"p:([1-9]{1})")
RE_D = re.compile(
    r"d:(((?:19|20)[0-9][0-9])-(0?[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01]))"
)


def get_files(files_path: Path = Path(".")) -> Iterator[Path]:
    """ Search for files in the given path. Currently it will filter
    .ipynb_checkpoints.
    """
    return filter(
        lambda x: not x.match("*/.ipynb_checkpoints/*"),
        files_path.glob("**/*.py")
    )


def parse_fields(tag_field: Optional[str]) -> tuple[int, str]:
    """ Parse/extract the 'p'riority and 'd'ate value from the tag field inside
    the brackets '<>'. Can have both or only one of the tags.
    Expects a string with the p or d tag and respetives values. 'p' should have
    a single integer 1-9 and 'd' should return a date in the format yyyy-mm-dd.

    Parameters
    ----------
    tag_field: str
    """

    priority = 1
    date = 'yyyy-mm-dd'

    if (tf := tag_field) and tf.strip() != '':
        if (p_match := RE_P.search(tag_field)):
            priority = p_match.group(1)

        if (d_match := RE_D.search(tag_field)):
            date = d_match.group(1)

    return priority, date


def search_files(files: Iterator[Path]) -> list[ParsedTags]:
    """ Search for tags """

    tags = select_tags()
    # search for comentaries with tags
    regex = re.compile(f'(?:(?:# )({tags})(?::))(.*?)(?:(?:<(.*?)>)|(?:\n))')

    findings = []
    for file in files:
        with file.open(mode='r') as f:
            for l_no, line in enumerate(f, start=1):
                if (match := regex.search(line)):
                    priority, date = parse_fields(match.group(3))

                    findings.append({
                        'path': str(file),
                        'tag': match.group(1),
                        'priority': str(priority),
                        'date': date,
                        'line': l_no,
                        'msg': match.group(2).strip(),
                     })

    return findings
