# split_fasta.py
# usage: to split the combined fasta into individual fasta
# Disuan & Wara & Rtiya: dn10tenz@gmail.com
# date: July 6th, 2013

#!/sw/bin/python2.7


from Bio import SeqIO #for Biopython & use SeqIO.functions 
import os #for use os.functions
import sys #for the arguments

the_fasta_file = sys.argv[1]
mydire = sys.argv[2]

print('Loading...') 
fastas = list(SeqIO.parse(the_fasta_file, "fasta")) 
n = input("Enter number of fasta_files to write of %i : " %len(fastas)) 
for i in range(n): 
    if n>len(fastas): 
        print('Error') 
        print('Loading...') 
        print('>>>Please try again<<<') 
        n = input("Enter number of fasta_files to write of %i : " %len(fastas)) 
if n<=len(fastas): 
    print('Please wait...') 
    fastas = SeqIO.parse(the_fasta_file, "fasta") #open file "1.GAC.454Reads_1-940-5_Ind3-DF.fna" 
    for line in range(n): #for loop 0-n 
        rec = fastas.next() #change files in fastafile 
        rec_n = rec 
        files = rec.id #Save fasta_name
        newname = files+'.fasta' #change name ... add '.fasta' from files
        print newname #show list files
        if not os.path.exists(mydire): 
            os.mkdir(mydire)  #create my directory 
            os.chdir(mydire)   #save in my directory
        with open(newname, "w") as out:  #create file  
            out.write(str(rec_n.id) + "\n")  #write fasta_id 
            out.write(str(rec_n.seq) + "\n") #write fasta_sequence 
        out.close()
        os.chdir('../')

print('\n##Done##')
    
