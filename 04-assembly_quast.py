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

    
    parser.add_argument('--input' ,'-i',required=True, help='Insert report.tsv from path:Service_folder /home/user/Service_folder/ANALYSIS/05-assembly/quast_all/report.tsv ')
    
    parser.add_argument('--output_bn','-b', required=True, help='The output in binary file')
    
    parser.add_argument('--output_csv','-c', required=True, help='The output in csv file')
    

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


def quast_dictionary_csv (quast_dict, csvfile):
    
    '''
    
    Description:
        Function to create a csv from a dictionary
    Input:
        quast_dict from previus funtion
    Return:
        quast_dict_csv
        
   '''
    
    dic     = quast_dict #Nested dictionary 
    parameters = sorted (list(list (dic.values())[0].keys()))  #Encabezado de las columnas

    with open(csvfile, "w") as f:
        w = csv.writer( f )
        w.writerow(['sample_name'] + parameters)# printea la primera fila

       
        for sample in dic.keys():
            #print (dic.keys())
            w.writerow([sample] + [dic[sample][parameter] for parameter in parameters])


            
#################
### FUNCTIONS ###
#################


def quast_dictionary_bn (quast_dict, quast_dict_bn):
    
    '''

    Description:
        Function to create a binary file from a dictionary
    Input:
        kmer_dict from previus funtion
    Return:
        kmer_dict_bn
    '''


    pickle_out = open(quast_dict_bn,"wb")
    pickle.dump(quast_dict, pickle_out)
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
    quast_dict = quast_dictionary (arguments.input)
    
    print ('quast_dict done')
    print (quast_dict)
    

    #Convert the dictionary to csv file
    
    quast_dictionary_csv (quast_dict, arguments.output_csv)
    
    print ('quast_dictionary_csv done')
   
  
         
    # Save the dicctionary to binary file
    
    quast_dictionary_bn (quast_dict, arguments.output_bn)
        
    print ('quast_dictionary_bn done')
            
 











            