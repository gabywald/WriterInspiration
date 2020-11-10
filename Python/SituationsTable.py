#!/usr/bin/python3
# -*- coding: utf-8 -*- 

import ModuleHelper
import re

class SituationsTable( object ) : 
    """This class defines SituationsTable Tables Definitions. """
    
    def __init__(self, name, description):
        """SituationsTable Constructor. """
        self.name = name
        self.description = description
        self.actors = description.split(", ")
    
    def __str__(self) : 
        """SituationsTable to str. """
        str = "SituationsTable ( '%s' ) \n"  % ( self.name )
        str += "\t description: %s \n" % (self.description)
        str += "\t actors: %s \n" % (self.actors)
        return str
    
    def appendVariant( self, variant ) : 
        """SituationsTable Variants """
        self.variants.append( variant )
    
    @classmethod
    def load( self ) : 
        tables = {}
        data = ModuleHelper.loadConfig( "36intriguesFondamentales" )
        nextTable = None
        for line in data : 
            if (not line.startswith("## ") ) : 
                resultTableHead = re.match( "^([0-9]+\. )(.*?) - (.*)$", line)
                if (resultTableHead != None) : 
                    if (nextTable != None) : 
                        tables[ nextTable.name ] = nextTable
                    nextTable = SituationsTable( resultTableHead.groups()[1], resultTableHead.groups()[2] )
        if (nextTable != None) : 
            tables[ nextTable.name ] = nextTable 
        return tables

