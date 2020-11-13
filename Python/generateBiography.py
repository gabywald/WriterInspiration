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

## ## ## ## ## Generate some Ideas from associated resources !

import random

from BiographicTable import BiographicTable
from BiographicTable import selectRandomBiographic
from BiographicTable import selectBiographicElements

biotables = BiographicTable.loadBiographicsTables()
jobs = BiographicTable.loadJobsToSkills()
talents = BiographicTable.loadSkills()

## print( biotables )
## print( selectRandomBiographic( biotables ) )
## print( jobs )
## for elt in jobs : 
##     print( jobs[ elt ] )
## print( talents )
## for elt in talents : 
##     print( talents[ elt ] )

res = selectBiographicElements( 3 )

for elt in res : 
    print( "%s => %s" %( ", ".join( elt.contents), ";".join( elt.addins ) ) )
