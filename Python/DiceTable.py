#!/usr/bin/python3
# -*- coding: utf-8 -*- 

import ModuleHelper
import re

class DiceTable( object ) : 
    """This class defines Dice Tables Definitions. """
    
    def __init__(self, name = None ):
        """DiceTable Constructor. """
        self.name = name
        self.subtables = []
        self.contents = []
    
    def __str__(self) : 
        """DiceTable to str. """
        str = "DiceTable ( '%s' ) \n"  % ( self.name )
        str += "\t subTables: %s \n" % (self.subtables)
        str += "\t contents: %s \n" % (self.contents)
        return str
    
    def appendSubTable( self, subtable ) : 
        """DiceTable SubTables """
        self.subtables.append( subtable )
    
    def appendContent( self, content ) : 
        """DiceTable Contents """
        self.contents.append( content )
    
    def getSubTable( self, name ) : 
        for sub in self.subtables : 
            if (name == sub.name) : 
                return sub
        return None
    
    @classmethod
    def load( self ) : 
        tables = {}
        data = ModuleHelper.loadFileConfig( "sousLesDesLideeJdR" )
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
        return tables
