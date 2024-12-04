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
module to generate the output of the findings
"""

from .utils import ParsedTags

def list_tags(
    findings: list[ParsedTags],
    sort_order: list[str] = BASE_ODER
) -> list[str]:
    """ """

    # sort each codetag entry
    findings.sort(key=itemgetter('path', 'tag', 'date', 'priority', 'line'))

    output = []

    printed_0, printed_1, printed_2, printed_3 = None, None, None, None

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
