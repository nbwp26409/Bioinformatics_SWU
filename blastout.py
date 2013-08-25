## blastout.py
## Usage : blast fasta_files from database 
## Disuan & Wara & Rtiya : dn10tenz@gmail.com
## Date : July 6th, 2013

from Bio.Blast.Applications import NcbiblastnCommandline
from Bio.Blast import NCBIXML
import os,fnmatch
import sys
import subprocess as SP

fastafiles = sys.argv[1] 
database = sys.argv[2]
directory = sys.argv[3]

for files in os.listdir(fastafiles):
    if fnmatch.fnmatch(files, '*.fasta'):
        openfiles = open(files)
        showname = openfiles.name[0:14]
        newname = str(directory)+str(showname)+'.xml'
                
        blastn = 'blastn'+' '+'-query'+' '+files+' '+'-db'+' '+database+' '+'-outfmt 5'+' '+'-out'+' '+newname
        runblast = os.system(str(blastn))
               
        print files
        

  		
        
        
        
        
        
        

        
    

         
        
