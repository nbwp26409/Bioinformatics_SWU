## denvtypesplit.py
## Usage for split xml files to each DENV? types
## Date : July 8th, 2013
## Disuan, Wara & Rtiya : dn10tenz@gmail.com

import os, fnmatch, re, shutil
import sys


directory = sys.argv[1]   #xml files directory

savemydires = sys.argv[2]  #create directory for savemydires


mydire = sys.argv[3]            #subdirectory in savemydires for create DENV? folders
mydire1 = sys.argv[4]
mydire2 = sys.argv[5]
mydire3 = sys.argv[6]

denv1 = "Dengue virus 1"  #types DENV? for search in xml files
denv2 = "Dengue virus 2"
denv3 = "Dengue virus 3"
denv4 = "Dengue virus 4"


if not os.path.exists(savemydires): #create new directory
    os.makedirs(savemydires)
    os.chdir(savemydires)

if not os.path.exists(mydire): #create new subdirectory
    os.makedirs(mydire)
    os.chdir(mydire)
os.chdir('../')

if not os.path.exists(mydire1):
    os.makedirs(mydire1)
    os.chdir(mydire1)
os.chdir('../')

if not os.path.exists(mydire2):
    os.makedirs(mydire2)
    os.chdir(mydire2)
os.chdir('../')

if not os.path.exists(mydire3):
    os.makedirs(mydire3)
    os.chdir(mydire3)
os.chdir('../..')


for files in os.listdir(directory):

    file = os.path.join(directory,files)
    #print file
    folder = os.path.join(directory,savemydires)
    #print folder
    newfiles = os.path.join(folder,mydire)
    #print newfiles
    newfiles1 = os.path.join(folder,mydire1)
    newfiles2 = os.path.join(folder,mydire2)
    newfiles3 = os.path.join(folder,mydire3)
    
    filescopied = os.path.join(folder,files)

    
    if fnmatch.fnmatch(files, '*.xml'):         #xml file only in my directory
        shutil.copy(files,folder)
        
         
        with open(filescopied, "r") as fileread:       #open files and read
            for line1 in fileread:               #loop file in directory   
                if re.findall(denv1,line1):      #findall str in file
                    shutil.copy(filescopied,newfiles)
                
                     
        with open(filescopied, "r") as fileread1:            
            for line2 in fileread1:
                if re.findall(denv2,line2):
                    shutil.copy(filescopied,newfiles1)
        

        with open(filescopied, "r") as fileread2:
            for line3 in fileread2:
                if re.findall(denv3,line3):
                    shutil.copy(filescopied,newfiles2)
                
        with open(filescopied, "r") as fileread3:
            for line4 in fileread3:
                if re.findall(denv4,line4):
                    shutil.copy(filescopied,newfiles3)
                

        print files


os.system('del'+' '+folder+'\\'+'*.xml')      



             
        
                
                    
                    
                
                                           
                    
                    
        
                    
                    
        
                
            
            
        
        

    
        
           
           
        
        
            
        
            
        
