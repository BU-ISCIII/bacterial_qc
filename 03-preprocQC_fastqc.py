#!/usr/bin/env python3


import argparse
import sys
import re
import csv
import pickle



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

    parser = argparse.ArgumentParser(prog = '03-preprocQC_fastqc.py', formatter_class=argparse.RawDescriptionHelpFormatter, description= '03-preprocQC_fastqc.py creates a csv file from fastqc.txt file')

    parser.add_argument('--path','-p', required=True, help='Insert path of fatsqc.txt file from 01-fastQC or 03-prepocQC folder like /home/user/Service_folder/ANALYSIS/01-fastQC or /home/user/Service_folder/ANALYSIS/03-prepocQC') 
                        
    parser.add_argument('--file' ,'-f',required=True, help='Insert type of lecture anlased from folder 01-fastQC:R1_fastqc/ or R2_fastqc/ and from folder 03-prepocQC: R1_filtered_fastqc/ or R2_filtered_fastqc/')                
                     
    parser.add_argument('--output','-o', required=True, help='The output')
  
    

    return parser.parse_args()



#################
### FUNCTIONS ###
#################


def fastqc_dict (file_txt):
    
    '''
    Description:
        Function to extract the relevant part of fastqc.txt file
    Input:
        fastqc.txt file
    Return:
        extracted_list
    '''
    
    step = '03-preprocQC_'
    qc_dict = {}
    header = False
    with open (file_txt, 'r') as fd:
        for line in fd:
            m = re.search ('END_MODULE',line)#te busca si esta la cadena
            if m:
                break
            m = re.search('FastQC', line)
            if header:
                line = line.replace('\n','') 
                line = line.split('\t')
                qc_dict[step + line[0]] = line[1]
            if m:
                header = True
    
    return qc_dict


#################
### FUNCTIONS ###
#################


def save_fatsqc_dic (qc_dict, file)

    pickle_out = open(file,"wb")
    pickle.dump(qc_dict, pickle_out)
    pickle_out.close()

return 

###################
### MAIN SCRIPT ###
###################


if __name__ == '__main__' :


    # Variables
    version = '03-preprocQC_fastqc v 0.1.0.'  # Script version
    
    # Create sample_id_list
    path = arguments.path
    sample_list = []
    tmp = os.listdir (path)
    for item in tmp:
        if os.path.isdir(os.path.join(path, item)):
        sample_list.append(item)

    print (sample_list)
    
    # Create a dictionary
    fastq_all = {}

    for sample in sample_list:
        
        file_name = os.path.join (path,sample,sample+arguments.file,"fastqc_data.txt")
        fastq_all[sample] = fastqc_dict (file_name)
        print (fastq_all)#nested dict
            
    # Save the dicctionary to file
    
    save_fatsqc_dic (fastq_all, arguments.output)
            
            