#!/usr/bin/env python

# Simulation to model demography on a landscape. This simulation 
# will include:
# - birth
# - death
# - dispersal

# First Version
# - Asexual reproduction
# - Annual generation times
# - Poisson-distributed number of offspring
# - Discrete landscape
# - Max dispersal of 1 grid
# - No diagonal dispersal
# - Equal probability of different directions
# - Non-zero probably of not dispersing
# - Starts in the middle
# - Start size of 50
# - No carrying capacity

# Object types
# - Individuals
# - Landscape
# - Cell

# Each generation first disperses, then reproduces

import numpy.random as nr 

# Class Definitions

class landscape:
    """This class holds all individuals across the landscape"""

    def __init__(self,nRows=5,nCols=5,startSize=50):
        """
        Creates a new grid-based with the number of rows, columns, and 
        starting population size specified by the user.
        """
        self.nRows = nRows
        self.nCols = nCols
        self.startSize = startSize
        self.sections = self.setup(self.nRows,self.nCols)
        for _ in range(self.startSize):
            self.sections[0][0].individuals.append(ind(myLandscape=self,myCell=self.sections[0][0]))


    def setup(self,nRows,nCols):
        """Sets up the landscape as a list of lists containing cells."""
        land = []
        for rowNum in range(nRows):
            row = []
            for colNum in range(nCols):
                row.append(cell(("%d_%d") % (rowNum,colNum)))
            land.append(row)
        return land

    def printLandscape(self):
        """Print all id numbers of cells in landscape"""
        for row in self.sections:
            for col in row:
                print("%d" % (len(col.individuals)), "\t", end="")
            print("\n")

class cell:
    """This class represents a grid square on our landscape."""

    def __init__(self,id):
        self.id = id
        self.individuals = []

class ind:
    """This class represents individuals in our population."""
    
    def __init__(self,myLandscape,myCell,name="",rowPos=0,colPos=0,disProb=0.5):
        self.myLandscape = myLandscape
        self.myCell = myCell
        self.name = name
        self.offspring = []
        self.meanOffNum = 2.0
        self.rowPos = rowPos
        self.colPos = colPos
        self.disProb = disProb

    def reproduce(self):
        """Return list of offspring"""
        numOff = nr.poisson(self.meanOffNum)
        offspringList = []
        for _ in range(numOff):
            offspringList.append(ind())
        return offspringList

    def disperse(self):
        """Move, if necessary, to new cell. disProb is dispersal probability."""
#randomly selected dispersal probability should be less than the set dispersal probability        
        if (nr.random() < self.disProb):
#for the cells at the middle of the landscape
            # Middle cell
            if (self.rowPos > 0) & (self.rowPos < self.myLandscape.nRows-1) & (self.colPos > 0) & (self.colPos < self.myLandscape.nCols-1):
                ranNum = nr.random()
#if dispersal probability is less than 0.25 individuals move up
                if (ranNum < 0.25):
                    self.rowPos = self.rowPos - 1
#if dispersal probability is less than 0.5 individuals move down
                elif (ranNum < 0.5):
                    self.rowPos = self.rowPos + 1
#if disp probability <0.75 ind move to the left
                elif (ranNum < 0.75):
                    self.colPos = self.colPos - 1
#else ind moves to the right
                else:
                    self.colPos = self.colPos + 1
#for cells in the upper left corner
            # Upper left cell
            elif (self.rowPos == 0) & (self.colPos == 0):
                ranNum = nr.random()
#if disp prob < 0.5 ind move down
                if (ranNum < 0.5):
                    self.rowPos = self.rowPos + 1
                else:
#else individual move to the right
                    self.colPos = self.colPos + 1
#for a cell on the left edge
            # Left edge cell
            elif (self.rowPos > 0) & (self.rowPos < self.myLandscape.nRows-1) & (self.colPos == 0):
                ranNum = nr.random()
#if disp prob <0.33 ind move up
                if (ranNum < 0.33):
                    self.rowPos = self.rowPos - 1
#if disp prob  <0.66 ind move doown
                elif (ranNum < 0.66):
                    self.rowPos = self.rowPos + 1
#else ind move to the right
                else:
                    self.colPos = self.colPos + 1
#for ind in cells at the bottom left
            # Bottom left cell
            elif (self.rowPos == self.myLandscape.nRows-1) & (self.colPos == 0):
                ranNum = nr.random()
#if disp prob <0.5  ind move up
                if (ranNum < 0.5):
                    self.rowPos = self.rowPos - 1
#else move  to the right
                else:
                    self.colPos = self.colPos + 1
#for ind in bottom edge cell
            # Bottom edge cell
            elif (self.rowPos == self.myLandscape.nRows-1) & (self.colPos > 0) & (self.colPos < self.myLandscape.nCols-1):
                ranNum = nr.random()
#if disp prob <0.33 ind move up
                if (ranNum < 0.33):
                    self.rowPos = self.rowPos - 1
                elif (ranNum < 0.66):
#if disp prob <0.66 ind move left
                    self.colPos = self.colPos - 1
#else ind move right
                else:
                    self.colPos = self.colPos + 1
#for ind in bottom right cell
            # Bottom right cell
            elif (self.rowPos == self.myLandscape.nRows-1) & (self.colPos == self.myLandscape.nCols-1):
                ranNum = nr.random()
#if disp prob <0.5 ind move up
                if (ranNum < 0.5):
                    self.rowPos = self.rowPos - 1
#else move left
                else:
                    self.colPos = self.colPos - 1
#for ind in right edge cell
            # Right edge cell
            elif (self.rowPos > 0) & (self.rowPos < self.myLandscape.nRows-1) & (self.colPos == self.myLandscape.nCols-1):
                ranNum = nr.random()
#if disp prob <0.33 ind move up
                if (ranNum < 0.33):
                    self.rowPos = self.rowPos - 1
#if disp prob <0.66 ind move down
                elif (ranNum < 0.66):
                    self.rowPos = self.rowPos + 1
#else ind move left
                else:
                    self.colPos = self.colPos - 1
#for ind in upper right corner cell
            # Upper right cell
            elif (self.rowPos == 0) & (self.colPos == self.myLandscape.nCols-1):
                ranNum = nr.random()
#if disp prob < 0.5 ind move down
                if (ranNum < 0.5):
                    self.rowPos = self.rowPos + 1
#else ind move to the left
                else:
                    self.colPos = self.colPos - 1
#for ind in upper edge cell, if disp prob >= self.disp prob
            # Upper edge cell
            else:
                ranNum = nr.random()
#if disp prob <0.33 ind move down
                if (ranNum < 0.33):
                    self.rowPos = self.rowPos + 1
#if disp prob <0.66 ind move left
                elif (ranNum < 0.66):
                    self.colPos = self.colPos - 1
#else ind move right
                else:
                    self.colPos = self.colPos + 1
#remove individuals from cell to enable dispersal and then append to the respective new cells and then\
# update the number of individuals in the new cells after dispersal
            self.myCell.individuals.remove(self)
            self.myLandscape.sections[self.rowPos][self.colPos].individuals.append(self)
            self.myCell = self.myLandscape.sections[self.rowPos][self.colPos]

# Run demographic simulation
# a landscape known as simlandscape is to be simulated using object landscape and ind distribution at generation 0 printed
simLandscape = landscape()
print("Generation 0:"); print()
simLandscape.printLandscape()

gens = 20
#show distribution of individuals in simlandscape over 20 generations
for g in range(gens):
    allIndividuals = []
#add individuals to respective sections in the landscape
    for r in range(simLandscape.nRows):
        for c in range(simLandscape.nCols):
            allIndividuals.extend(simLandscape.sections[r][c].individuals)
#let the individuals disperse and print out the landscape after dispersal and the generation number
    for i in allIndividuals:
        i.disperse()

    print("Generation %d:" % (g+1)); print()

    simLandscape.printLandscape()
