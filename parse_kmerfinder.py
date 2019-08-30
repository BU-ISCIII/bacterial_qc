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

    parser = argparse.ArgumentParser(prog = '07-kmerfinder.py', formatter_class=argparse.RawDescriptionHelpFormatter, description= '07-kmerfinder.py creates a csv file from results.txt file')

    parser.add_argument('--path','-p', required=True, help='Insert path of results.txt file like /home/user/Service_folder/ANALYSIS/07-kmerfinder')

    parser.add_argument('--output_bn','-b', required=True, help='The output in binary file')

    parser.add_argument('--output_csv','-c', required=True, help='The output in csv file')



    return parser.parse_args()



#################
### FUNCTIONS ###
#################


def kmerfinder_dictionary (file_txt):

    '''
    Description:
        Function to extract the relevant part of result.txt file
    Input:
        result.txt file
    Return:
        dictionary
    '''

    step = '07-kmerfinder_'

    num_lines = sum(1 for line in open (file_txt))
    hits = (num_lines - 1) #to count the total number of hits

    lookupfile = open (file_txt, 'r')
    lines = lookupfile.readlines()
    parameters = lines[0].strip().split("\t")
    if num_lines > 1:
        values_best_hit = lines[1].strip().split("\t")
    if num_lines >2:
        values_second_hit = lines[2].strip().split("\t")


    kmer_dict ={}


    for i in range (len(parameters)):
        if num_lines > 1:
            kmer_dict[step + 'best_hit_' + parameters [i]] = values_best_hit [i]
        else:
            kmer_dict [step + 'best_hit_' + parameters [i]] = ''

        if num_lines >2:

            kmer_dict [step + 'second_hit_' + parameters [i]] = values_second_hit [i]

        else:

            kmer_dict [step + 'second_hit_' + parameters [i]] = ''

        kmer_dict.update(Total_hits_07_kmerfinder = hits)
    return kmer_dict


#################
### FUNCTIONS ###
#################


def kmerfinder_dictionary_bn (kmer_dict, kmer_dict_bn):

    '''

    Description:
        Function to create a binary file from a dictionary
    Input:
        kmer_dict from previus funtion
    Return:
        kmer_dict_bn
    '''


    pickle_out = open(kmer_dict_bn,"wb")
    pickle.dump(kmer_dict, pickle_out)
    pickle_out.close()

    return


#################
### FUNCTIONS ###
#################


def kmerfinder_dictionary_csv (kmer_all, kmer_dict_csv, sample_list):

    '''

    Description:
        Function to create a csv from a dictionary
    Input:
        kmer_dict from previus funtion
    Return:
        kmer_dict_csv

    '''

    headers = sorted(list(list (kmer_all.values())[0].keys()))
    #import pdb; pdb.set_trace()
    with open(kmer_dict_csv, "w") as f:
        w = csv.writer(f)
        w.writerow(['sample_name'] + headers)

        for sample in sample_list:

            w.writerow([sample] + [kmer_all[sample][param] for param in headers])
    return



###################
### MAIN SCRIPT ###
###################


if __name__ == '__main__' :


    # Variables
    version = '07-kmerfinder.py v 0.1.0.'  # Script version
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
    #print (sample_list)

    # Create a dictionary
    kmer_all = {}


    for sample in sample_list:

        file_name = os.path.join (path,sample,"results.txt")
        kmer_all[sample] = kmerfinder_dictionary(file_name)




    print ('kmerfinder_dictionary done')
    #print (kmer_all)


    # Save the dicctionary to binary file

    kmerfinder_dictionary_bn (kmer_all, arguments.output_bn)

    print ('kmerfinder_dictionary_bn done')

    # Convert the dictionary to csv file

    kmerfinder_dictionary_csv (kmer_all, arguments.output_csv, sample_list)

    print ('kmerfinder_dictionary_csv done')









