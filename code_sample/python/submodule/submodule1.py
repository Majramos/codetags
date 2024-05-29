#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  submodule1.py
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
This is a sample module for developing/testing codetags
"""

# NOTE: 'note' out of functions, submodule1, line 29, no closing brackets 

# NOTE: 'note' multirow, out of functions, submodule1, line 31, no closing brackets 
# 'note' multirow, out of functions, submodule1, line 31, no closing brackets

# TODO: 'todo' out of functions, submodule1, line 34, with closing brackets <>

class Aclass():
    
    # BUG: 'bug' in class, submodule1, line 38, brackets date 2022-01-01, multirow
    # 'bug' in class, submodule1, line 38, brackets date 2022-01-01, multirow <d:2022-01-01>
    
    def __init__(self, arg1: str='test'):
        """ Lorem ipsum dolor sit amet, consectetur adipiscing elit. In 
        bibendum nisl vitae dolor maximus volutpat. In ac est faucibus, 
        pulvinar neque ultricies, mattis neque.
        
        Parameter
        ---------
        arg1 : str
        """
        # TODO: 'todo' in method, submodule1, line 47, no closing brackets 
        self.arg1 = arg1


def a_function() -> None: 
    """ Lorem ipsum dolor sit amet, consectetur adipiscing elit. In 
    bibendum nisl vitae dolor maximus volutpat. In ac est faucibus, 
    pulvinar neque ultricies, mattis neque.
    
    """
    # normal coment, do not include
    a_object = Aclass() # FIXME: 'fixme' in function, submodule1, line 61, no brackets 
    
    return a_object
    
    
def another_function() -> None: 
    """ Lorem ipsum dolor sit amet, consectetur adipiscing elit. In 
    bibendum nisl vitae dolor maximus volutpat. In ac est faucibus, 
    pulvinar neque ultricies, mattis neque.
    
    """
    
    a_object = Aclass() # TODO: 'todo' in function, submodule1, line 73, brackets p2, multiline
    # 'todo' in function, submodule1, line 73, brackets p2, multiline <p:2>
    
    # normal coment, do not include
    return a_object


def main() -> None:
    """ Lorem ipsum dolor sit amet, consectetur adipiscing elit. In 
    bibendum nisl vitae dolor maximus volutpat. In ac est faucibus, 
    pulvinar neque ultricies, mattis neque.
    
    """
    
    # FIXME: 'fixme' in function 'main', submodule1, line 87, with brackets p1 <p:1>
    a_function() # normal coment, do not include


if __name__ == "__main__":
    main()
