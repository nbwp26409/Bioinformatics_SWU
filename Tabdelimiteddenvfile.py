#tabdelimiteddenv1file.py
#usage create tab delimited file for open on excel
#Disuan, Wara & Rty : dn10tenz@gmail.com
#July 25th, 2013 :fixed July 30th, 2013

from Bio.Blast import NCBIXML
from string import maketrans
from numpy import *
import os
import csv, re, sys, fnmatch
from Bio import SeqIO


denv1 = "Dengue virus 1"	
denv2 = "Dengue virus 2"
denv3 = "Dengue virus 3"
denv4 = "Dengue virus 4"

A = 'A'
T = 'T'
C = 'C'
G = 'G'
dat = '-'

denvfile = sys.argv[1] #file database :can choose ==> DENV1.fasta, DENV2.fasta, DENV4.fasta, or DENV4.fasta
directory = sys.argv[2] #Directory .xml files
newfilename = sys.argv[3] #newfilename for insert header to file

filename =  'tabtest.txt'#filename for create tab file
	
opendenv = open(denvfile) #open denv file for use row of array
readdenv = SeqIO.parse(denvfile, 'fasta') 

length = ''
for i in readdenv: 
	length = len(i) #length of template

arr = zeros((length,7)) #create array low is length
denvtype = input('\n'+'Please choose denvtype(denv1, denv2, denv3 or denv4) same denvfile : ') #choose denvtype for create denv? tab delimited file 
	
for location in range(length): #for Position of header in tab file
	arr[location,[0]] = location+1

for files in os.listdir(directory):
	if fnmatch.fnmatch(files, '*.xml'):
		openfile = open(files)
		openxml = NCBIXML.parse(openfile)
		for record in openxml:
			for alignments in record.alignments:
				for hsp in alignments.hsps:
					if denvtype in str(alignments): #Specify denvtype :denv1, denv2, denv3 or denv4
						startq = hsp.query_start
						endq = hsp.query_end
						hspsq = hsp.query
						hspsh = hsp.sbjct
						startfrom = hsp.sbjct_start
						endto = hsp.sbjct_end

						reverse_hspsq = hspsq[::-1] 
						reverse_hspsh = hspsh[::-1] 

						
						if startfrom < endto: #somefiles start position < end position 
							for j,query in enumerate(hspsq,start = startfrom-1): #startfrom-1 :because start from 0 + header
								for i in A:
									if A == query:
										arr[j,[1]] += 1
								for k in T:
									if T == query:
										arr[j,[2]] += 1
								for l in C:
									if C == query:
										arr[j,[3]] += 1
								for m in G:
									if G == query:
										arr[j,[4]] += 1
								for n in dat:
									if dat == query:
										arr[j,[5]] += 1
							for s,hseq in enumerate(hspsh,start = startfrom-1):
								for o in dat:
									if dat == hseq:
										arr[s,[6]] += 1
						if startfrom > endto: #somefiles start position > end position 
							for ji,requery in enumerate(reverse_hspsq,start = endto-1): #use reverse_hspsq : because start from end 
								for ii in A:
									if A == requery:
										arr[ji,[1]] += 1
								for ki in T:
									if T == requery:
										arr[ji,[2]] += 1
								for li in C:
									if C == requery:
										arr[ji,[3]] += 1
								for mi in G:
									if G == requery:
										arr[ji,[4]] += 1
								for ni in dat:
									if dat == requery:
										arr[ji,[5]] += 1
							for si,rehseq in enumerate(reverse_hspsh,start = endto-1):
								for oi in dat:
									if dat == rehseq:
										arr[si,[6]] += 1

createdfile = open(filename, 'w') #create file for write

string = '' 

for row in arr:
	for col in row:
		L = str((int(col))) 
		string = string + L +'\t'  
		cuttab = string.strip() #cut the last tab(\t) 
	string = cuttab + '\n' 
createdfile.write(string) #write data to file

createdfile.close()

headers = ['Position','A','T','C','G','Deletion','Insertion'] #headers
newfile = open(newfilename+'.txt','w') #create newfile
oldfile = open(filename, 'r') #open oldfile for write data to new file
newfile.write('\t'.join(headers) + '\n') #add or join header to newfile
for line in string:
	newfile.write(line)

oldfile.close() 
newfile.close()

os.remove(filename) #remove oldfile and because got new file



















                            
                                        				                 			

                    		                   	




						


																
							


								

				

				
						

					


				





						
