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

#import libraries
import numpy.random as nr 

# Class Definitions
#create the landscape class 
class landscape:
    """This class holds all individuals across the landscape"""
#define what the landscape will contain: number of rows/columns
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
            self.sections[0]
#puts the starting number of individuals in the first cell
[0].individuals.append(ind(myLandscape=self,myCell=self.sections[0][0]))

#for each of the number of rows add the number of columns add the row/col number
#also, add the row number to the list land
    def setup(self,nRows,nCols):
        """Sets up the landscape as a list of lists containing cells."""
        land = []
        for rowNum in range(nRows):
            row = []
            for colNum in range(nCols):
                row.append(cell(("%d_%d") % (rowNum,colNum)))
            land.append(row)
        return land
#prints the landscape and for each row/col print the number of individuals in that cell
    def printLandscape(self):
        """Print all id numbers of cells in landscape"""
        for row in self.sections:
            for col in row:
                print("%d" % (len(col.individuals)), "\t", end="")
            print("\n")
#class used to contain information about each cell. 
class cell:
    """This class represents a grid square on our landscape."""
#each cell contains a number of individuals
    def __init__(self,id):
        self.id = id
        self.individuals = []
#Class conains information about the individuals in each cell
class ind:
    """This class represents individuals in our population."""
#Each individual get a position(row/col),a proablity of moving to next cell,avg number of offspring
    def __init__(self,myLandscape,myCell,name="",rowPos=0,colPos=0,disProb=0.1):
        self.myLandscape = myLandscape
        self.myCell = myCell
        self.name = name
        self.offspring = []
        self.meanOffNum = 2.0
        self.rowPos = rowPos
        self.colPos = colPos
        self.disProb = disProb
#The number of offspring each indiviual has determined by a poisson using the avg. num of offspring defined
    def reproduce(self):
        """Return list of offspring"""
        numOff = nr.poisson(self.meanOffNum)
        offspringList = []
        for _ in range(numOff):
            offspringList.append(ind())
        return offspringList
#Used to move the individuals to other cells, using random number and disersal probability
    def disperse(self):
        """Move, if necessary, to new cell. disProb is dispersal probability."""
        if (nr.random() < self.disProb):

            # Middle cell
#determines if the individual will move
            if (self.rowPos > 0) & (self.rowPos < self.myLandscape.nRows-1) & (self.colPos > 0) & (self.colPos < self.myLandscape.nCols-1):
#if the conditions above are true then the following is used to determine which direction the individuals will move            
		ranNum = nr.random()
#if the ranom number is less than .25 or greater than .75 the individual will move to the left one cell.
#if the random number is less than.5 or other it moves to the right one cell.
                if (ranNum < 0.25):
                    self.rowPos = self.rowPos - 1
                elif (ranNum < 0.5):
                    self.rowPos = self.rowPos + 1
                elif (ranNum < 0.75):
                    self.colPos = self.colPos - 1
                else:
                    self.colPos = self.colPos + 1
#deterimes direction ind will move if in upper left cell
            # Upper left cell
            elif (self.rowPos == 0 & self.colPos == 0):
                ranNum = nr.random()
                if (ranNum < 0.5):
                    self.rowPos = self.rowPos + 1
                else:
                    self.colPos = self.colPos + 1
#deterimes direction ind will move if in left cell
            # Left edge cell
            elif (self.rowPos > 0) & (self.rowPos < self.myLandscape.nRows-1) & (self.colPos == 0):
                ranNum = nr.random()
                if (ranNum < 0.33):
                    self.rowPos = self.rowPos - 1
                elif (ranNum < 0.66):
                    self.rowPos = self.rowPos + 1
                else:
                    self.colPos = self.colPos + 1
#deterimes direction ind will move if in bottom left cell
            # Bottom left cell
            elif (self.rowPos == self.myLandscape.nRows-1) & (self.colPos == 0):
                ranNum = nr.random()
#deterimes direction ind will move if in botton cell            
            # Bottom edge cell
            elif (self.rowPos == self.myLandscape.nRows-1) & (self.colPos > 0) & (self.colPos < self.myLandscape.nCols-1):
                ranNum = nr.random()
                if (ranNum < 0.33):
                    self.rowPos = self.rowPos - 1
                elif (ranNum < 0.66):
                    self.colPos = self.colPos - 1
                else:
                    self.colPos = self.colPos + 1
#deterimes direction ind will move if in bottom right cell
            # Bottom right cell
            elif (self.rowPos == self.myLandscape.nRows-1) & (self.colPos == self.myLandscape.nCols-1):
                ranNum = nr.random()
                if (ranNum < 0.5):
                    self.rowPos = self.rowPos - 1
                else:
                    self.colPos = self.colPos - 1
#deterimes direction ind will move if in right cell
            # Right edge cell
            elif (self.rowPos > 0) & (self.rowPos < self.myLandscape.nRows-1) & (self.colPos == self.myLandscape.nCols-1):
                ranNum = nr.random()
                if (ranNum < 0.33):
                    self.rowPos = self.rowPos - 1
                elif (ranNum < 0.66):
                    self.rowPos = self.rowPos + 1
                else:
                    self.colPos = self.colPos - 1
#deterimes direction ind will move if in upper right cell
            # Upper right cell
            elif (self.rowPos == 0) & (self.colPos == self.myLandscape.nCols-1):
                ranNum = nr.random()
                if (ranNum < 0.5):
                    self.rowPos = self.rowPos + 1
                else:
                    self.colPos = self.colPos - 1
#deterimes direction ind will move if in upper cell
            # Upper edge cell
            else:
                ranNum = nr.random()
                if (ranNum < 0.33):
                    self.rowPos = self.rowPos + 1
                elif (ranNum < 0.66):
                    self.colPos = self.colPos - 1
                else:
                    self.colPos = self.colPos + 1

            self.myCell.individuals.remove(self)
            self.myLandscape.sections[self.rowPos][self.colPos].individuals.append(self)
            self.myCell = self.myLandscape.sections[self.rowPos][self.colPos]

# Run demographic simulation

simLandscape = landscape()
print("Generation 0:"); print()
simLandscape.printLandscape()

gens = 10
#for the number of generations all the individuals are put in cells(rows and columns)
for g in range(gens):
    allIndividuals = []
    for r in range(simLandscape.nRows):
        for c in range(simLandscape.nCols):
            allIndividuals.extend(simLandscape.sections[r][c].individuals)
#for each generation move individuals to next cell
    for i in allIndividuals:
        i.disperse()

    print("Generation %d:" % (g+1)); print()
#print the number of individuals in the landscape
    simLandscape.printLandscape()
