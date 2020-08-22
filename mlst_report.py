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

    parser = argparse.ArgumentParser(prog = 'mlst_report.py', formatter_class=argparse.RawDescriptionHelpFormatter, description= 'mlst_report.py creates a csv file from results.txt file')

    parser.add_argument('--path','-p', required=True, help='Insert path of results.txt file like /home/user/Service_folder/08-mlst_ariba/run')

    parser.add_argument('--output_csv','-c', required=True, help='The output in csv file')



    return parser.parse_args()

 #Example:python3 mlst_report.py -p /home/bioinfomicro/bioinfomicro/Servicios/Brucella/08-mlst_ariba/run/ -c mlst_all.csv

#################
### FUNCTIONS ###
#################


def mlst_dictionary (file_txt):

    '''
    Description:
        Function to extract the relevant part of result.txt file
    Input:
        result.txt file
    Return:
        dictionary
    '''

    step = '08-mlst_ariba_'

    lookupfile = open (file_txt, 'r')
    lines = lookupfile.readlines()
    parameters = lines[0].strip().split("\t")
    values = lines[1].strip().split("\t")

    mlst_dict ={}


    for i in range (len(parameters)):

        mlst_dict[parameters [i]] = values [i]
        

    return mlst_dict


#################
### FUNCTIONS ###
#################


def mlst_dictionary_csv (mlst_all, mlst_dict_csv, sample_list):

    '''
    Description:
        Function to create a csv from a dictionary
    Input:
        kmer_dict from previus funtion
    Return:
        kmer_dict_csv
    '''

    headers = sorted(list(list (mlst_all.values())[0].keys()))
    
    with open(mlst_dict_csv, "w") as f:
        w = csv.writer(f)
        w.writerow(['sample_name'] + headers)

        for sample in sample_list:

            w.writerow([sample] + [mlst_all[sample][param] for param in headers])
    return



###################
### MAIN SCRIPT ###
###################


if __name__ == '__main__' :


    # Variables
    version = '08-mlst_ariba.py v 0.1.0.'  # Script version
    arguments = check_arg(sys.argv[1:])

    # Create sample_id_list
    path = arguments.path
    sample_list = []
    tmp = os.listdir (path)
    for item in tmp:
        if os.path.isdir(os.path.join(path, item)):
            if item != 'logs':
                sample_list.append(item)

    print ('sample_list done')
    print (sample_list)

    # Create a dictionary
    mlst_all = {}


    for sample in sample_list:
        file_name = os.path.join (path,sample,sample +".MLSTS.out.run","mlst_report.tsv")
        print (file_name)
        mlst_all[sample] = mlst_dictionary(file_name)

    print ('mlst_dictionary done')
    #print (mlst_all)

    # Convert the dictionary to csv file

    mlst_dictionary_csv (mlst_all, arguments.output_csv, sample_list)
    print ('mlst_dictionary_csv done')
