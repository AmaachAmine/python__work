#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Created at 01/26/2019 by Amine Amaach
# Object -> "electronic diary" : a program that emulates a diary

# creating the main record class (optional:practice purpose)
import os
class record:
    def __init__(self,date,time,person,place,note):
        self.date = date # date of the record
        self.time = time # time of creating this record
        self.person = person # name of the person to meet 
        self.place = place # the meeting place
        self.note = note # a note about the record


# ## Defining functions :

# ### Menu() : it shows the menu and returns the choice of the user

# In[3]:


def Menu():
    os.system('clear')
    choices = [1,2,3,4,5,0]
    print('\n\tMENU :')
    print('1 -> Add record ')
    print('2 -> Edit record ')
    print('3 -> Delete record ')
    print('4 -> Display whole record sorted by date ')
    print('5 -> Search for a specific record ')
    print('0 -> Exit ')
    
    # get the user's choice :
    try:
        choice = int(input('Choose your choice : '))
    except ValueError: # this is for handling the valueError if the the user entred non-int type
        print('\nPlease select one choice from the menu below :')
        choice = Menu()
        return choice # this statement is so important : it means if we had that error So there is no need to proceed
                      # in the parent function "which calls its self"
        
    # verification of choice, it has to be between [1-5]
    if choice in choices:
        return choice
    else:
        # TODO : os.system('clear') screen
        print('\nPlease select one choice from the menu below :')
        Menu()
        


# ### dateValidat() : a function that validats the date entred by the user 

# In[4]:


def dateValidat():
    os.system('clear')
    import datetime
    today = datetime.datetime.now().strftime("%x")
    print('\ntoday date : ' + today)

    date = str(input('Please Enter a valid date for the record Month/Day/Year : '))
    MonthDayYear = date.split('/')
    
    try:
        Month = int(MonthDayYear[0])
        Day = int(MonthDayYear[1])
        Year = int(MonthDayYear[2])
    except ValueError:
        print('\n!! inValid date !!')
        date = dateValidat()
        return date # this statement is so important : it means if we had that error So there is no need to proceed
                    # in the parent function "which calls its self"
    except IndexError:
        print('\n!! inValid date !!')
        date = dateValidat()
        return date
        
    while Day > 31 or Month > 12 or Year < 19:
        print('\n!! inValid date !!')
        date = str(input("Please Enter a valid date for the record e.g : %s " %today))
        MonthDayYear = date.split('/')
        Month = int(MonthDayYear[0])
        Day = int(MonthDayYear[1])
        Year = int(MonthDayYear[2])
    return date


# ### isExist() : this function return True is the record exist else it returns False  

# In[5]:


def isExist(pattern):
    with open('records') as f:
        contents = f.read()
        records = contents.split('\n')
    for record in records:
        if pattern in record:
            return True,record
    return False 


# ### addRecord(): adds records, and it's responsable of creating the data base if doesn't exist already 

# In[6]:


def addRecord():
    os.system('clear')
    # I'm using the default type of the file which is txt
    try:
        f = open('records','x')
    except FileExistsError: 
        f = open('records','a')
    finally:
        print('\n\t\tADD RECORD :')
        # creation time :
        import datetime
        time = datetime.datetime.now().strftime("%X")
        # getting the data about the record :
        date = dateValidat()
        # person name :
        person = str(input('What is the name of the person : '))
        # meeg place :
        place = str(input('Meeting place :'))
        # note about the meeting :
        note = str(input('Write a note about s meeting :'))
        
        # create a record object :
        myRecord = record(date,time,person,place,note)
        
        recordLine = str(myRecord.__dict__) + '\n'
        recordLine = recordLine.replace("'",' ').replace('{','').replace('}','')
        f.write(recordLine)

        f.close()
        print('\nThe record is successfully saved\n')


# ### getPattern() : this function returns in which function the user wants to change the record

# In[7]:


def getPattern():
    os.system('clear')
    # Getting the pattren to search for :
    # time or date of the record are mandatory to find the record
    pattern = str()

    print("\nHow do you like to select the record :")
    print("\t1 -> By Date ")
    print("\t2 -> By person's Name ")
    print("\t3 -> By meeting place ")
    try:
        choice = int(input("What would you like to do : "))
    except ValueError:
        print("\n\t!! Wrong Choice !! try again : ")
        pattern = getPattern()
        return pattern
    
    if choice == 1 :
        pattern = dateValidat()
        return pattern
    elif choice == 2 :
        pattern = input("Person's name : ") 
        return pattern
    elif choice == 3 :
        pattern = input("Meeting place : ") 
        return pattern
    else:
        print("\n\t!! Wrong Choice !! try again : ")
        pattern = getPattern()
        return pattern


# ### editRecord() : edit record in function of date,time,person's name, and/or meeting place

# In[8]:


def editRecord():
    os.system('clear')
    print('\n\t\tEDIT RECORD :')
    pattern = getPattern()
    
    while len(pattern) == 0:
        again = input('\ninValid pattern, Try again(n/y) : ')
        if again == 'y':
            pattern = getPattren()
        else:
            print('\nExiting... ')
            return
    
    proceed,record = isExist(pattern)
    record = record.split(',')
    
    if not proceed :
        print("\n!! RECORD DOESN'T EXIST !!")
        print('Returning to Menu ...')
        return
        
    with open('records') as f:
        newFile = str()
        newTime = newDate = newPerson = newPlace = str()
        print('\nWhat do you like to change : ')
        print("\t1 -> Date ")
        print("\t2 -> Person's Name ")
        print("\t3 -> Meeting place ")
        try:
            choice = int(input("What would you like to do : "))
        except ValueError:
            print("\n\t!! Wrong Choice !! Exiting... ")
            return

        if choice == 1:
            print('\nWhat is the new date : ')
            new = dateValidat()
            # old date :
            oldDate = record[0].split(':')
            old = oldDate[1]
        elif choice == 2:
            new = input("What is the new person's name : ")
            # old name :
            oldName = record[2].split(':')
            old = oldName[1]
        elif choice == 3:
            new = input('What is the new meeting place : ')
            # old place :
            oldPlace = record[3].split(':')
            old = oldPlace[1]
        else:
            print("\n\t!! Wrong Choice !! Exiting... ")
            return          
        newFile = ''
        for line in f:
            if pattern not in line:
                newFile = newFile + line
            else:
                line = line.replace(old,new)
                newFile = newFile + line

    with open('records','w') as f:
        f.write(newFile)
    print('The record is succesfully changed')
    


# ### displayRecord() : shows the user a specific record 

# In[22]:


def displayRecord():
    os.system('clear')
    print('\n\t\tDISPLAY RECORD :')
    pattern = getPattern()
    
    while len(pattern) == 0:
        again = input('\ninValid pattern, Try again(n/y) : ')
        if again == 'y':
            pattern = getPattren()
        else:
            print('\nExiting... ')
            return
    try:
        proceed,record = isExist(pattern)
    except TypeError: 
        print("\n!! RECORD DOESN'T EXIST !!")
        print('Returning to Menu ...')
        return

    record = record.split(',')
    
    if not proceed :
        print("\n!! RECORD DOESN'T EXIST !!")
        print('Returning to Menu ...')
        return
    
    date = record[0].split(':')
    time = record[1].split(' ')
    person = record[2].split(':')
    place = record[3].split(':')
    note = record[4].split(':')
    print('\nTime of creation  : %s' %time[5])
    print('Date of the record : %s' %date[1])
    print("Person's name : %s " %person[1])
    print("Meeting place : %s " %place[1])
    print("Note  : %s " %note[1])
    
    again = 'y'
    while again == 'y':
        again = input('Display another record (n/y) :')
        if again == 'y':
            displayRecord()
            break
        else:
            return
            
    
    


# ### deleteRecord() : delete a specific record.

# In[10]:


def deleteRecord():
    os.system('clear')
    print('\n\tDELETE RECORD :')
    pattern = getPattern()
    
    while len(pattern) == 0:
        again = input('\ninValid pattern, Try again(n/y) : ')
        if again == 'y':
            pattern = getPattren()
        else:
            print('\nExiting... ')
            return
    
    proceed,record = isExist(pattern)
    
    if not proceed :
        print("\n!! RECORD DOESN'T EXIST !!")
        print('Returning to Menu ...')
        return 
    
    with open('records') as src:
        try:
            f = open('temp','x')
        except FileExistsError:
            f = open('temp','a')
        finally:
            for line in src:
                if pattern in line:
                    continue
                    print(line)   
                else:
                    f.write(line)
                    
                    
        f.close()
            
    import os 
    os.remove('records')
    os.rename('temp','records')
    
    print('\nThe record was succesfully deleted')
    


# ### execute() : The main function that executes all functions of the project dependes on user's choice 

# In[11]:


def execute():
    choice = Menu()
    while choice in [0,1,2,4,5]:
        if choice == 0:
            return
        elif choice == 1:
            addRecord()
            choice = Menu()
        elif choice == 2:
            editRecord()
            choice = Menu()
        elif choice == 3:
            deleteRecord()
            choice = Menu()
        elif choice == 4:
            pass
        elif choice == 5:
            displayRecord()
            choice = Menu()
        


# In[26]:


execute()

