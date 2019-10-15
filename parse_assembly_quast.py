#!/usr/bin/env python3


import argparse
import sys
import re
import csv
import pickle
import os


#################
### FUNCTIONS ###
#################


def check_arg (args=None) :

    '''
	Description:
        Function collect arguments from command line using argparse
    Input:
        args # command line arguments
    Constant:
        None
    Variables
        parser
    Return
        parser.parse_args() # Parsed arguments
    '''

    parser = argparse.ArgumentParser(prog = '04-assembly_quast.py', formatter_class=argparse.RawDescriptionHelpFormatter, description= '04-assembly_quast.py creates a csv file from report.tsv file.')

    
    parser.add_argument('--path' ,'-p',required=True, help='Insert report.tsv from path:Service_folder /home/user/Service_folder/ANALYSIS/05-assembly/quast_all/report.tsv ')
    
    parser.add_argument('--output_bn','-b', required=True, help='The output in binary file')
    
    parser.add_argument('--output_csv','-c', required=True, help='The output in csv file')
    
    #Example: python3 parse_assembly_quast.py -p /home/s.gonzalez/SRVCNM046_20170717_NEISSERIAG-II_RA_S/ANALYSIS/05-assembly/quast_all/report.tsv -b p_dic.bn -c p_assembly.csv
    
    return parser.parse_args()



#################
### FUNCTIONS ###
#################


def quast_dictionary (file_tsv):

    '''
    Description:
        Function to create a dictionary from quast_all/report.tsv file
    Input:
        report.tsv file
    Return:
        quast_dict (dictionary)
    '''


    lookupfile = open (file_tsv, 'r')
    lines = lookupfile.readlines()
    samples = lines[0].strip().split("\t")
    samples = samples [1:]#samples_id
    lookup = lines [1:]
    quast_dict ={}

    for line in lookup:
        line = line.strip()
        dic = line.split("\t")
        parameter = dic [0]
        parameter = (parameter + '_Assembly_quast_all')#add the name of the step
        for i in range (len(samples)):
            if not samples[i] in quast_dict:
                quast_dict [samples [i]] = {} 
            quast_dict[samples [i]] [parameter] = dic [i+1]
        
    return quast_dict#nested dictionary


#################
### FUNCTIONS ###
#################


def dictionary2csv (dictionary, csv_file):

    '''

    Description:
        Function to create a csv from a dictionary
    Input:
        dictionary
    Return:
        csv file

   '''


    header = sorted(set(i for b in map(dict.keys, dictionary.values()) for i in b))
    with open(csv_file, 'w', newline="") as f:
        write = csv.writer(f)
        write.writerow(['sample', *header])
        for a, b in dictionary.items():
            write.writerow([a]+[b.get(i, '') for i in header])

#################
### FUNCTIONS ###
#################


def dictionary2bn (dictionary, binary_file):

    '''

    Description:
        Function to create a binary file from a dictionary
    Input:
        dictionary
    Return:
        binary file
    '''


    pickle_out = open(binary_file,"wb")
    pickle.dump(dictionary, pickle_out)
    pickle_out.close()

    return

###################
### MAIN SCRIPT ###
###################



if __name__ == '__main__' :


    # Variables
    version = '04-assembly_quast_all v 0.2.0.'  # Script version
    arguments = check_arg(sys.argv[1:])
    
    # Create a dictionary
    quast_dict = quast_dictionary (arguments.path)
    
    print ('quast_dict done')
    #print (quast_dict)
    
    #Convert the dictionary to csv file
    
    dictionary2csv (quast_dict, arguments.output_csv)
    
    print ('quast_dictionary_csv done')
   
         
    # Save the dicctionary to binary file
    
    dictionary2bn (quast_dict, arguments.output_bn)
        
    print ('quast_dictionary_bn done')
            
 











            