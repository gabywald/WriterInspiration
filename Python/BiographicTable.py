#!/usr/bin/python3
# -*- coding: utf-8 -*- 

import ModuleHelper
import re

class BiographicTable( object ) : 
    """This class defines Tables Definitions for 'biographic' elements for Curriculum generation. """
    
    def __init__(self, name = None, comments = None ):
        """BiographicTable Constructor. """
        self.name = name
        self.comments = comments
        self.contents = []
        self.linksTo  = []
        self.addins   = []
    
    def __str__(self) : 
        """BiographicTable to str. """
        str = "BiographicTable ( % s , % s ) \n"  % (self.name, self.comments)
        str += "\t contents: %s \n" % (self.contents)
        str += "\t linksTo: %s \n" % (self.linksTo)
        str += "\t addins: %s \n" % (self.addins)
        return str
    
    def appendContent( self, content) : 
        self.contents.append( content )
    
    def appendLinks( self, link) : 
        self.linksTo.append( link )
    
    def appendAddin( self, addin) : 
        self.addins.append( addin )
    
    @classmethod
    def load( self ) : 
        tables = {}
        data = ModuleHelper.loadConfig( "biographyCyberAge" )
        nextTable = None
        nextSubTable = None
        for line in data : 
            resultTableHead = re.match( "^Table (.*?)(\t(.*?))?(\t(.*?))?$", line)
            resultTableContent = re.match( "^\t(.*?)(\t\[(.*?)\])?(\t\{(.*?)\})?$", line )
            if (resultTableHead != None) : 
                if (nextTable != None) : 
                    tables[ nextTable.name ] = nextTable
                nextTable = BiographicTable( resultTableHead.groups()[0], resultTableHead.groups()[2] )
                ## print ( resultTableHead.groups() )
            elif (resultTableContent != None) : 
                nextTable.appendContent( resultTableContent.groups()[0] );
                nextTable.appendLinks( resultTableContent.groups()[2] );
                nextTable.appendAddin( resultTableContent.groups()[4] );
        if (nextTable != None) : 
            tables[ nextTable.name ] = nextTable 
        return tables

class BiographicElement( object ) : 
    def __init__(self, content, comments ):
        self.content    = content
        self.addins     = []

def selectRandomBiographic() : 
    """Choose randomly an element from a randomly choosen BiographicTable. """
    pass
