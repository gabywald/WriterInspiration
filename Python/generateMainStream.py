#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = "Gabriel Chandesris"
__copyright__ = "CC Gabriel Chandesris (2020)"
__credits__ = ""
__licence__ = "GNU GENERAL PUBLIC LICENSE v3"
__version__ = "0.1.0"
__maintainer__ = "Gabriel Chandesris"
__email__ = "gabywald[at]laposte.net"
__contact__ = "gabywald[at]laposte.net"
__status__ = "Development"

## ## ## ## ## Generate some Ideas from associated resource : "36intriguesFondamentales.txt" !

import random

from SituationsTable import SituationsTable

tables = SituationsTable.load()

## print( tables )

numberOfResults = 3

for i in range(0, numberOfResults) : 
    result = random.choice( list(tables.items()) )
    print( "***** %s *****" % ( result[0] ) )
    if ( len(result[1].actors) > 1) : 
        print( "\t Avec : ", *result[1].actors, sep = "\n\t\t" )

