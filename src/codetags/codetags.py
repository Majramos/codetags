#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  codetags.py
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

"""

"""


import re
from pathlib import Path
from operator import itemgetter
from typing import TypedDict, Optional


TAGS: list[str] = ['BUG', 'FIXME', 'NOTE', 'TODO']

BASE_ODER: list['str'] = ['path', 'tag', 'date', 'priority']



class ParsedTags(TypedDict):
    path = str
    tag = str
    priority = int
    date = str
    line = int 
    msg = str



class CodeTags:

    def __init__(self):
        pass

    def __repr__(self):
        return f'CodeTags(l={self.loc}, o={self.output}, s={self.sort}, t={self.tag})'

    def select_files(self):
        return self

    def search_tags(self):
        return self

    def list_tags(self):
        return self

    def print_findings(self):
        return None
        
    def write_findings(self):
        return None
 

def get_files(loc=None):
    """ Search for files """

    CWD = Path()/'code_sample'
    files = list(CWD.glob('**/*2.py'))

    return files


def select_tags(selection=None) -> str:
    """ Select which tags to search for """

    if selection:
        return '|'.join(selection)
    else:
        return '|'.join(TAGS)


RE_P = re.compile(r'p:([1-9]{1})')
RE_D = re.compile(r'd:(((?:19|20)[0-9][0-9])-(0?[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01]))')

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


def search_files(files: list[Path]) -> list[ParsedTags]:
    """ Search for tags """ 

    tags = select_tags()
    # search for comentaries with tags
    regex1 = re.compile(f'(?:(?:# )({tags})(?::))(.*?)(?:(?:<(.*?)>)|(?:\n))')

    findings = []
    for file in files:
        with file.open(mode='r') as f:
            for l_no, line in enumerate(f, start=1):
                if (match := regex1.search(line)):
                    priority, date = parse_fields(match.group(3))

                    findings.append({
                        'path': str(file), 
                        'tag': match.group(1),
                        'priority': str(priority),
                        'date': date,
                        'line': l_no, 
                        'msg': match.group(2).strip(),
                     })

    # print(findings)
    return findings


def list_tags(findings: list[ParsedTags], sort_order: list[str]=BASE_ODER) -> list[str]:
    """ """

    # sort each codetag entry
    findings.sort(key=itemgetter('path', 'tag', 'date', 'priority', 'line'))

    output = []

    printed_0, printed_1, printed_2, printed_3 = None, None, None,None

    for values in findings:
        p0, p1, p2, p3, p4, p5 = values.values()
        # print('{0} {1:<5} {2} {3} {4:<4} {5}'.format(p0, p1, p2, p3, p4, p5))

        if p0 != printed_0:
            output.append(p0)
            printed_0 = p0
            printed_1 = None
        if p1 != printed_1:
            output.append(f'{"":2}{p1}')
            printed_1 = p1
            printed_2 = None
        if p2 != printed_2:
            output.append(f'{"":4}{p2}')
            printed_2 = p2
            printed_3 = None
        if p3 != printed_3:
            output.append(f'{"":6}{p3}')
            printed_3 = p3

        output.append(f'{"":8} l:{p4:4} > {p5}')

    return output


def print_findings(findings: list[str]) -> None:
    """ print the findings """

    for f in findings:
        print(f)
