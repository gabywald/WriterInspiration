#!/usr/bin/python3
# -*- coding: utf-8 -*- 

import ModuleHelper
import re
import random

class BiographicTable( object ) : 
    """This class defines Tables Definitions for 'biographic' elements for Curriculum generation. """
    _tables = None
    
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
        if (self._tables != None) : 
            return self._tables
        self._tables = {}
        data = ModuleHelper.loadConfig( "biographyCyberAge" )
        nextTable = None
        nextSubTable = None
        for line in data : 
            resultTableHead = re.match( "^Table (.*?)(\t(.*?))?(\t(.*?))?$", line)
            resultTableContent = re.match( "^\t(.*?)(\t\[(.*?)\])?(\t\{(.*?)\})?$", line )
            if (resultTableHead != None) : 
                if (nextTable != None) : 
                    self._tables[ nextTable.name ] = nextTable
                nextTable = BiographicTable( resultTableHead.groups()[0], resultTableHead.groups()[2] )
                ## print ( resultTableHead.groups() )
            elif (resultTableContent != None) : 
                nextTable.appendContent( resultTableContent.groups()[0] );
                nextTable.appendLinks( resultTableContent.groups()[2] );
                nextTable.appendAddin( resultTableContent.groups()[4] );
        if (nextTable != None) : 
            self._tables[ nextTable.name ] = nextTable 
        return self._tables

class BiographicElement( object ) : 
    def __init__(self, name ):
        self.contents = []
        self.contents.append( name )
        self.addins = []
    
    def __str__(self) : 
        """BiographicElement to str. """
        str = "BiographicElement () \n" 
        str += "\t contents: %s \n" % (self.contents)
        str += "\t addins: %s \n" % (self.addins)
        return str

class BiographicMetier( object ) : 
	_list = None
    ## TODO BiographicMetier (load, getrandom...)
    pass

class BiographicTalent( object ) : 
    _list = None
    ## TODO BiographicMetier (load, getrandom...)
    pass

def selectRandomBiographic( tables ) : 
    """Choose randomly an element from a randomly choosen BiographicTable. """
    orientation = tables[ "d'Orientation" ]
    ## print( orientation )
    bioELT = None
    while (orientation != None) : 
        contents = orientation.contents
        links = orientation.linksTo
        addins = orientation.addins
        index = random.randint(0, len(contents) - 1 )
        ## print( "%d (%d, %d, %d)" %( index, len(contents), len(links), len(addins) ) )
        content = contents[index]
        link = links[index]
        addin = addins[index]
        ## ## ## Generate / complete a BiographicElement 
        if (bioELT == None) : 
            bioELT = BiographicElement( content )
        else : 
            bioELT.contents.append( content )
        if (addin != None) : 
            bioELT.addins = addin.split( ";" )
        if (link != None) : 
            if (link == "Cicatrices") : 
                orientation = tables[ "Cicatrices-localisation" ]
                bioELT.contents.append( "Cicatrice : %s" %( random.choice( orientation.contents ) ) )
                orientation = tables[ "Cicatrices-gravité" ]
                bioELT.contents.append( "Cicatrice : %s" %( random.choice( orientation.contents ) ) )
                orientation = None;
            else:
                orientation = tables[ link ];
        else : 
            orientation = None
    ## print( bioELT )
    return bioELT

def selectBiographicElements( number ) : 
    results = []
    tables = BiographicTable.load()
    for i in range(0, number) : 
        results.append( selectRandomBiographic( tables ) )
    return results

