#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  utils.py
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
Module to store constants and utilities
"""

from typing import TypedDict


TAGS: tuple[str] = ("BUG", "FIXME", "NOTE", "TODO")

BASE_ODER: tuple[str] = ("path", "tag", "date", "priority")


def select_tags(selection: list[str] = TAGS) -> str:
    """ Select which tags to search for in the code, these will be used as input
    in a regular expression

    Returns
    -------
    a string of the selected tags concatenated with a '|'
    """

    return '|'.join(selection)


class ParsedTags(TypedDict):
    path = str
    tag = str
    priority = int
    date = str
    line = int
    msg = str
