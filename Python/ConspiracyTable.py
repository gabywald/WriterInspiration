#!/usr/bin/python3
# -*- coding: utf-8 -*- 

import ModuleHelper
import re
import random

class ConspiracyTable( object ) : 
    """This class defines ConspiracyTable Tables Definitions. """
    
    def __init__(self, name):
        """ConspiracyTable Constructor. """
        self.name = name
        self.contents = []
    
    def __str__(self) : 
        """ConspiracyTable to str. """
        str = "ConspiracyTable ( '%s' ) \n"  % ( self.name )
        str += "\t contents: %s \n" % (self.contents)
        return str
    
    def appendContent( self, content ) : 
        """ConspiracyTable Contents """
        self.contents.append( content )
    
    @classmethod
    def load( self ) : 
        tables = {}
        data = ModuleHelper.loadConfig( "complots" )
        nextTable = None
        for line in data : 
            if (not line.startswith("## ") ) : 
                resultTableHead = re.match( "^Table (.*?)$", line)
                resultTableContent = re.match( "^\t(.*?)$", line )
                if (resultTableHead != None) : 
                    if (nextTable != None) : 
                        tables[ nextTable.name ] = nextTable
                    nextTable = ConspiracyTable( resultTableHead.groups()[0] )
                elif (resultTableContent != None) : 
                    nextTable.appendContent( resultTableContent.groups()[0] );
        if (nextTable != None) : 
            tables[ nextTable.name ] = nextTable 
        return tables
    
    @classmethod
    def generateSomeConspiracy( self ) : 
        tables = ConspiracyTable.load()
        sentence = random.choice( tables[ "Conspiracy" ].contents )
        toBeReplaced = re.findall( "([A-Z]{2,})", sentence)
        for elt in toBeReplaced: 
            print( elt )
            sentence = sentence.replace(elt, random.choice( tables[ elt ].contents ), 1)
        return sentence


