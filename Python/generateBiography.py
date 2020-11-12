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

## ## ## ## ## Generate some Ideas from associated resource : "biographyCyberAge.txt" !

import random

from BiographicTable import BiographicTable
from BiographicTable import selectRandomBiographic
from BiographicTable import selectBiographicElements

tables = BiographicTable.load()

## print( tables )
## print( selectRandomBiographic( tables ) )

res = selectBiographicElements( 3 )

for elt in res : 
    print( "%s => %s" %( ", ".join( elt.contents), ";".join( elt.addins ) ) )

