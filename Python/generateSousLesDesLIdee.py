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

## ## ## ## ## Generate some Ideas from associated resource !

import ModuleHelper
import re, random

from DiceTable import DiceTable

tables = {}
types = []

data = ModuleHelper.loadConfig( "sousLesDesLideeJdR" )

nextTable = None
nextSubTable = None
for line in data : 
    resultTableHead = re.match( "^Table (.*?)$", line)
    resultSubTableHead = re.match( "^\t(.*?)$", line )
    resultSubTableContent = re.match( "^\t\t(.*?)$", line )
    if (resultTableHead != None) : 
        if (nextTable != None) : 
            nextTable.appendSubTable( nextSubTable )
            tables[ nextTable.name ] = nextTable
            nextSubTable = None
        nextTable = DiceTable( resultTableHead.groups()[0] )
    elif ( (resultSubTableContent != None) and (nextSubTable != None) ) : 
        nextSubTable.appendContent( resultSubTableContent.groups()[0] )
    elif ( (resultSubTableHead != None) ) : 
        if (nextSubTable != None) : 
            nextTable.appendSubTable( nextSubTable )
        nextSubTable = DiceTable( resultSubTableHead.groups()[0] )
if (nextTable != None) : 
    tables[ nextTable.name ] = nextTable 
if (nextSubTable != None) : 
    nextTable.appendSubTable( nextSubTable ) 
 
## print( tables )
## for table in tables : 
##     print ( "\t%s\t%s" %( table, tables[ table ] ) )
##     for subtable in tables[ table ].subtables : 
##         print ( "\t\t%s" %( subtable ) )

## ## ## ## ## Retrieves the types of universe of playing / writing
for elt in tables[ "Personnages" ].subtables : 
    if elt.name not in types: 
        types.append( elt.name )

for elt in tables[ "Lieux" ].subtables : 
    if elt.name not in types: 
        types.append( elt.name )

## print ( types )

## ## ## ## ## Choose randomly
universe = random.choice ( types )

print ( "Choice is '%s'" %( universe ) )

personnaes = tables[ "Personnages" ].getSubTable( universe ).contents
locations = tables[ "Lieux" ].getSubTable( universe ).contents

## print ( personnaes )
## print ( locations )

## print ( tables[ "Interactions" ] )
## for subtable in tables[ "Interactions" ].subtables : 
##     print ( "\t\t%s" %( subtable ) )

interactions1 = tables[ "Interactions" ].getSubTable( "Entre personnages" ).contents
interactions2 = tables[ "Interactions" ].getSubTable( "Personnages et lieux" ).contents

numberOfResults = random.randint(5, 10)

for i in range(0, numberOfResults) : 
    result = []
    result.append( random.choice( personnaes ) )
    if (random.randint(0, 42)%2 == 0) : 
        result.append( random.choice ( interactions1 ) )
        result.append( random.choice ( personnaes ) )
    else: 
        result.append( random.choice ( interactions2 ) )
        result.append( random.choice ( locations ) )
    print ( " ".join( result ) )








