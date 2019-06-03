#!/usr/bin/env python3


import argparse
import sys
import re
import json


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

    parser = argparse.ArgumentParser(prog = 'Script_Sara.py', formatter_class=argparse.RawDescriptionHelpFormatter, description= 'Scrip_Sara.py creates a xxx  in a json format.')

    parser.add_argument('--input' ,'-i',required=True, help='There is a proper file')
    parser.add_argument('--output','-o', required=True, help='The output')

    return parser.parse_args()



#################
### FUNCTIONS ###
#################



def extract_list (file_txt):

    '''
    Description:
        Function to extract the relevant part of fastqc.txt file
    Input:
        fastqc.txt file
    Constant:
        None
    Variables:
        None
    Return:
        extracted_list
    '''


    extracted_list = [] #Empty list
    header = False
    with open (file_txt, 'r') as fd:
        for line in fd:
            m = re.search ('END_MODULE',line)
            if m:
                break
            m = re.search('FastQC', line)
            if header:
                line = line.replace('\n','')
                extracted_list.append (line)
            if m:
                header = True
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
    Constant:
        None
    Variables:
        None
    Return:
        fastqc_dict

    '''

    fastqc_dict = {}
    for item in extracted_list:
        fastqc_dict[item.split('\t')[0]] = item.split('\t')[1]
    return fastqc_dict


###################
### MAIN SCRIPT ###
###################

if __name__ == '__main__' :


    # Variables
    version = 'relevant_fastqc_text v1.0'  # Script version
    arguments = ""                        # Arguments from ArgParse

    # Grab arguments
    arguments = check_arg(sys.argv[1:])
    extracted_list = extract_list (arguments.input)
    print (extracted_list)

    # Create a dictionary
    fastqc_dict = fastqc_dictionary (extracted_list)
    print (fastqc_dict)

    # Convert the python dictionary above into a JSON string that can be written into a file

    with open (arguments.output,"w") as json_fastqc_dict:
        json.dump(fastqc_dict,json_fastqc_dict,indent=4)
        json_fastqc_dict.close()
        print (json_fastqc_dict)


