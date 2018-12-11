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
#Defining what the landscape is made of
    def __init__(self,nRows=5,nCols=5,startSize=50):
        """
        Creates a new grid-based with the number of rows, columns, and 
        starting population size specified by the user.
        """
        self.nRows = nRows
        self.nCols = nCols
        self.startSize = startSize
        self.sections = self.setup(self.nRows,self.nCols)
        #Making the Starting Population 0
        for _ in range(self.startSize):
            self.sections[0][0].individuals.append(ind(myLandscape=self,myCell=self.sections[0][0]))

#Numbering the columbs and rows
    def setup(self,nRows,nCols):
        """Sets up the landscape as a list of lists containing cells."""
        land = []
        for rowNum in range(nRows):
            row = []
            for colNum in range(nCols):
                row.append(cell(("%d_%d") % (rowNum,colNum)))
            land.append(row)
        return land
#Prints the Population for each columb and Row
    def printLandscape(self):
        """Print all id numbers of cells in landscape"""
        for row in self.sections:
            for col in row:
                print("%d" % (len(col.individuals)), "\t", end="")
            print("\n")
#Setting information about each Square in the Grid
class cell:
    """This class represents a grid square on our landscape."""

    def __init__(self,id):
        self.id = id
        self.individuals = []

class ind:
    """This class represents individuals in our population."""
    #each Individual in the Population is getting information applied to them about thier row position, columb position and Probability of thier predicted movement.
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
        #Setting the number of Offspring each individual has
        numOff = nr.poisson(self.meanOffNum)
        offspringList = []
        for _ in range(numOff):
            offspringList.append(ind())
        return offspringList

    def disperse(self):
        """Move, if necessary, to new cell. disProb is dispersal probability."""
        #Random Poission to move individuals around the Landscape
        if (nr.random() < self.disProb):
##setting limits to determine which way the individual moves for each position in the landscape
            # Middle cell
            if (self.rowPos > 0) & (self.rowPos < self.myLandscape.nRows-1) & (self.colPos > 0) & (self.colPos < self.myLandscape.nCols-1):
                ranNum = nr.random()
                if (ranNum < 0.25):
                    self.rowPos = self.rowPos - 1
                elif (ranNum < 0.5):
                    self.rowPos = self.rowPos + 1
                elif (ranNum < 0.75):
                    self.colPos = self.colPos - 1
                else:
                    self.colPos = self.colPos + 1

            # Upper left cell
            elif (self.rowPos == 0) & (self.colPos == 0):
                ranNum = nr.random()
                if (ranNum < 0.5):
                    self.rowPos = self.rowPos + 1
                else:
                    self.colPos = self.colPos + 1

            # Left edge cell
            elif (self.rowPos > 0) & (self.rowPos < self.myLandscape.nRows-1) & (self.colPos == 0):
                ranNum = nr.random()
                if (ranNum < 0.33):
                    self.rowPos = self.rowPos - 1
                elif (ranNum < 0.66):
                    self.rowPos = self.rowPos + 1
                else:
                    self.colPos = self.colPos + 1

            # Bottom left cell
            elif (self.rowPos == self.myLandscape.nRows-1) & (self.colPos == 0):
                ranNum = nr.random()
                if (ranNum < 0.5):
                    self.rowPos = self.rowPos - 1
                else:
                    self.colPos = self.colPos + 1
            
            # Bottom edge cell
            elif (self.rowPos == self.myLandscape.nRows-1) & (self.colPos > 0) & (self.colPos < self.myLandscape.nCols-1):
                ranNum = nr.random()
                if (ranNum < 0.33):
                    self.rowPos = self.rowPos - 1
                elif (ranNum < 0.66):
                    self.colPos = self.colPos - 1
                else:
                    self.colPos = self.colPos + 1

            # Bottom right cell
            elif (self.rowPos == self.myLandscape.nRows-1) & (self.colPos == self.myLandscape.nCols-1):
                ranNum = nr.random()
                if (ranNum < 0.5):
                    self.rowPos = self.rowPos - 1
                else:
                    self.colPos = self.colPos - 1

            # Right edge cell
            elif (self.rowPos > 0) & (self.rowPos < self.myLandscape.nRows-1) & (self.colPos == self.myLandscape.nCols-1):
                ranNum = nr.random()
                if (ranNum < 0.33):
                    self.rowPos = self.rowPos - 1
                elif (ranNum < 0.66):
                    self.rowPos = self.rowPos + 1
                else:
                    self.colPos = self.colPos - 1

            # Upper right cell
            elif (self.rowPos == 0) & (self.colPos == self.myLandscape.nCols-1):
                ranNum = nr.random()
                if (ranNum < 0.5):
                    self.rowPos = self.rowPos + 1
                else:
                    self.colPos = self.colPos - 1

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

gens = 20
#IDK what this next part is
for g in range(gens):
    allIndividuals = []
    for r in range(simLandscape.nRows):
        for c in range(simLandscape.nCols):
            allIndividuals.extend(simLandscape.sections[r][c].individuals)
#Move each person to new Square on landscape
    for i in allIndividuals:
        i.disperse()
#print the Population
    print("Generation %d:" % (g+1)); print()

    simLandscape.printLandscape()
