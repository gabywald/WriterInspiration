#!/usr/bin/python3
# -*- coding: utf-8 -*- 

import ModuleHelper
import re

class RPGsituationsTable( object ) : 
    """This class defines RPGsituations Tables Definitions. """
    
    def __init__(self, name, description):
        """RPGsituationsTable Constructor. """
        self.name = name
        self.description = description
        self.variants = []
    
    def __str__(self) : 
        """RPGsituationsTable to str. """
        str = "RPGsituationsTable ( '%s' ) \n"  % ( self.name )
        str += "\t description: %s \n" % (self.description)
        str += "\t variants: %s \n" % (self.variants)
        return str
    
    def appendVariant( self, variant ) : 
        """RPGsituationsTable Variants """
        self.variants.append( variant )
    
    @classmethod
    def load( self ) : 
        tables = {}
        data = ModuleHelper.loadConfig( "36intriguesJdR" )
        nextTable = None
        for line in data : 
            if (not line.startswith("## ") ) : 
                resultTableHead = re.match( "^(.*?) - (.*)$", line)
                resultTableVariant = re.match( "^\t(.*?)$", line )
                if (resultTableHead != None) : 
                    if (nextTable != None) : 
                        tables[ nextTable.name ] = nextTable
                    nextTable = RPGsituationsTable( resultTableHead.groups()[0], resultTableHead.groups()[1] )
                elif ( (resultTableVariant != None) and (nextTable != None) ) : 
                    nextTable.appendVariant( resultTableVariant.groups()[0] )
        if (nextTable != None) : 
            tables[ nextTable.name ] = nextTable 
        return tables

