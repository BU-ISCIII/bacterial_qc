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

    parser = argparse.ArgumentParser(prog = '03-preprocQC_fastqc.py', formatter_class=argparse.RawDescriptionHelpFormatter, description= '03-preprocQC_fastqc.py creates a csv file from fastqc.txt file.')

    parser.add_argument('--sample_name','-s', required=True, help='Insert sample_name: folow by the sample id number, e.g.sample_name:BNS6436')
    parser.add_argument('--input' ,'-i',required=True, help='Insert fastqc_data.txt from path:Service_folder/ANALYSIS/03-preprocQC/sample_id/sample_id_R1_filtered_fastqc/')
    parser.add_argument('--output','-o', required=True, help='The output (csv file)')
    

    return parser.parse_args()



#################
### FUNCTIONS ###
#################


def extract_list (file_txt, sample_name):

    '''
    Description:
        Function to extract the relevant part of fastqc.txt file
    Input:
        fastqc.txt file
    Return:
        extracted_list
    '''


    extracted_list = [] 
    header = False
    with open (file_txt, 'r') as fd:
        for line in fd:
            m = re.search ('END_MODULE',line)
            if m:
                break
            m = re.search('FastQC', line)
            if header:
                line = line.replace('\n','')
                extracted_list.append ('03-preprocQC_'+line) # add the name of the step in each parameter
            if m:
                header = True
                sample_name = sample_name.replace (':', '\t')
                extracted_list.append (sample_name) 
    return extracted_list


#################
### FUNCTIONS ###
#################


def fastqc_dictionary (extracted_list):

    '''

    Description:
        Function to create a dictionary from a list
    Input:
        extracted_list from previus funtion
    Return:
        fastqc_dict

    '''

    fastqc_dict = {}
    for item in extracted_list:
        fastqc_dict[item.split('\t')[0]] = item.split('\t')[1]
    return fastqc_dict


#################
### FUNCTIONS ###
#################  


def fastqc_dictionary_csv (fastqc_dict, csvfile):

    '''

    Description:
        Function to create a csv from a dictionary
    Input:
        fastqc_dict from previus funtion
    Return:
        fastqc_dict_csv
    '''

    
    with open(csvfile,'w') as f:
        w = csv.writer(f)
        w.writerow(fastqc_dict.keys())
        w.writerow(fastqc_dict.values())
        



###################
### MAIN SCRIPT ###
###################


if __name__ == '__main__' :


    # Variables
    version = '03-preprocQC_fastqc v 0.1.0.'  # Script version
    
    # Create list
    arguments = check_arg(sys.argv[1:])
    extracted_list = extract_list (arguments.input, arguments.sample_name)
    
    print ('extracted_list done')
       
    # Create a dictionary
    fastqc_dict = fastqc_dictionary (extracted_list)
    
    print ('fastqc_dict done')
            
    #Convert the dictionary to csv file
    
    fastqc_dictionary_csv (fastqc_dict, arguments.output)
    
    print ('fastqc_dictionary_csv done')
            
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



