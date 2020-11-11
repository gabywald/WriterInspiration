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

## ## ## ## ## Generate some Ideas from associated resource : "36intriguesDeJdR.txt" !

import random

from RPGsituationsTable import RPGsituationsTable

tables = RPGsituationsTable.load()

## print( tables )

numberOfResults = 2

for i in range(0, numberOfResults) : 
    result = random.choice( list(tables.items()) )
    print( "***** %s ***** %s //" % ( result[0], result[1].description ) )
    variantSelection = random.randint(0, len(result[1].variants) + 5 )
    if ( variantSelection < len(result[1].variants) ) : 
         print( "\tVariante: %s // // " %( result[1].variants[variantSelection] ) )

