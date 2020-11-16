#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = "Gabriel Chandesris"
__copyright__ = "CC Gabriel Chandesris (2020)"
__credits__ = ""
__licence__ = "GNU GENERAL PUBLIC LICENSE v3"
__version__ = "1.0.0"
__maintainer__ = "Gabriel Chandesris"
__email__ = "gabywald[at]laposte.net"
__contact__ = "gabywald[at]laposte.net"
__status__ = "Development"

## ## ## ## ## Generate some Conspiracy from associated resources !

from ConspiracyTable import ConspiracyTable

tables = ConspiracyTable.load()

print( tables )
for elt in tables : 
    print( tables[ elt ] )

print( ConspiracyTable.generateSomeConspiracy() )