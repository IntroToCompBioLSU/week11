#!/usr/bin/env python

class course(object):
    """
    This class defines a college course in which a student might enroll.
    """

    # Most courses are 3 credit hours, so we set that as a default.
    # if a class is not a 3 credit hour course, it must be specified.
    # The other fields do not have natural defaults.
    
    #initiating the those variable that will be present with in a course for use of classification.

    def __init__(self,name="",hours=3,instructor="",room=""):
        self.name = name
        self.hours = hours
        self.instructor = instructor
        self.room = room
        self.studentNames = []     # List to store course roster
        self.grades = {}           # Dictionary to store student grades
        
    def addStudent(self,newStudent):
        if newStudent not in self.studentNames:   # Only add student names if they're not currently on roster
            self.studentNames.append(newStudent)

# addStudent prevents student names from being added more than once and add additional sudents.

# defining the variables used drafting the information found in a roster per individual.

    def printRoster(self):
        print("The current roster for " + self.name + " includes:")
        for student in self.studentNames:
            print(student)

# Updates student grades.

    def updateStudentGrade(self,studentName,grade):
        self.grades[studentName] = grade

# Makes Updated Grade Available for viewing.

    def reportStudentGrade(self,studentName):
        print(self.grades[studentName])

# initiating a class to hold the information of individual students, which can be retrieved for use of add individuals to classes and the roster.
            
class studentRecord(object):
    """
    This class is an example of a student record that might be stored by a registrar.
    """
    
    def __init__(self,name,DOB,ID):
        self.name = name
        self.DOB = DOB
        self.ID = ID
        self.courses = [] # Add classes as the student enrolls
        
# defines the command to print all information in association with a students record.

    def printRecord(self):
        print("Name: "+self.name)
        print("DOB: "+self.DOB)
        print("ID: "+self.ID)
        print("Courses: ")
        for course in self.courses:
            print("  "+course.name)
    
# allows for a new course option to be added.
    
    def addCourse(self,course):
        if course not in self.courses:    # Only add course if it's not already there
            self.courses.append(course)
            
# List of courses available along with their associated information used for record information.

compPhylo = course(name="Computational Phylogenetics",instructor="Jeremy Brown",room="LSB 248")
uwb = course(name="Underwater Basket Weaving",instructor="Scuba Steve",room="Natatorium")
improv = course(name="Improvisational Comedy",hours=2,instructor="Stephen Colbert",room="Ed Sullivan Theater")
cellbio = course(name="Cell Biology",hours=3,instructor="Jamey Johnson",room="Grand Ole Opry")

# List of students ad their associated information which is used to retain their information in records.

chuck = studentRecord(name="Charles Darwin",DOB="12 February 1809",ID="1859")
ron = studentRecord(name="Sir Ronald Aylmer Fisher",DOB="17 February 1890",ID="1930")
lane = studentRecord(name="Lane Bazar",DOB="21 December 1995",ID="89039")

# Naturally, both of these students are interested in phylogenetics. We'll begin by adding them to the course roster.
# This will add a students name to the a course of choice.

compPhylo.addStudent(chuck.name) # Darwin's name is added to the CompPhylo roster
compPhylo.addStudent(ron.name)   # Now Fisher's name is added
compPhylo.addStudent(lane.name)

# This adds a course to each of their student records

chuck.addCourse(compPhylo)  # Note that we're passing a course object as an argument here
ron.addCourse(compPhylo)
lane.addCourse(compPhylo)

# Fisher also wants to take improv comedy, while Darwin is interested in basket weaving

improv.addStudent(ron.name)
ron.addCourse(improv)

uwb.addStudent(chuck.name)
chuck.addCourse(uwb)

cellbio.addStudent(lane.name)
lane.addCourse(cellbio)

# Check course rosters
# prints the current roster

print("**** CHECKING COURSE ROSTERS ****"); print()
for course in [compPhylo,uwb,improv,cellbio]:
    course.printRoster()
    print()
    
# Now check student records
# prints the current student records

print("**** CHECKING STUDENT RECORDS ****"); print()
for student in [chuck,ron,lane]:
    student.printRecord()
    print()
