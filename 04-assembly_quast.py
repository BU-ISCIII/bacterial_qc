#!/usr/bin/env python3


import argparse
import sys
import re
import csv



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

    
    parser.add_argument('--input' ,'-i',required=True, help='Insert report.tsv from path:Service_folder/ANALYSIS/05-assembly')
    parser.add_argument('--output','-o', required=True, help='The output (csv file)')
    

    return parser.parse_args()



#################
### FUNCTIONS ###
#################


def quast_dictionary (file_txt):

    '''
    Description:
        Function to create a dictionary from quast_all/report.tsv file
    Input:
        report.tsv file
    Return:
        quast_dict (dictionary)
    '''


    lookupfile = open (file_txt, 'r')
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


def quast_dictionary_csv (quast_dict, csvfile):
    
    '''
    
    Description:
        Function to create a csv from a dictionary
    Input:
        quast_dict from previus funtion
    Return:
        quast_dict_csv
        
    '''
    
    headers = quast_dict.values()[0].keys() 
    with open(csvfile, "wb") as f:
        w = csv.writer( f )
        w.writerow(['sample_name'] + headers)
        parameters = headers
        for sample in quast_dict.keys():
            w.writerow([sample] + [quast_dict[sample][parameter] for parameter in parameters])
    
    

###################
### MAIN SCRIPT ###
###################



if __name__ == '__main__' :


    # Variables
    version = '04-assembly_quast_all v 0.1.0.'  # Script version
    
    # Create a dictionary
    arguments = check_arg(sys.argv[1:])
    quast_dict = quast_dictionary (arguments.input)
    
    print (quast_dict)   

    #Convert the dictionary to csv file
    
    quast_dictionary_csv (quast_dict, arguments.output)
    
    print (quast_dictionary_csv)
            
 











            