#!/usr/bin/python3
# -*- coding: utf-8 -*- 

class DiceTable( object ) : 
    """This class defines Tables Definitions. """
    
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
