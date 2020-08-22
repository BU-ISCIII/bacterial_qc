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

    parser = argparse.ArgumentParser(prog = 'parse_kraken.py', formatter_class=argparse.RawDescriptionHelpFormatter, description= 'parse_kraken.py creates a csv file from results.txt file')

    parser.add_argument('--path','-p', required=True, help='Insert path of results.txt file like /home/user/Service_folder/ANALYSIS/07-kraken')

    parser.add_argument('--output_bn','-b', required=True, help='The output in binary file')

    parser.add_argument('--output_csv','-c', required=True, help='The output in csv file')

   #Example: python3 parse_kraken.py -p /home/bioinfomicro/bioinfomicro/Servicios/Brucella/kraken -b p_dic.dicke -c kraken_all_componente1.csv

    return parser.parse_args()



#################
### FUNCTIONS ###
#################


def kraken_dictionary (file_txt):

    '''
    Description:
        Function to extract the relevant part of result.txt file
    Input:
        result.txt file
    Return:
        dictionary
    '''

    step = '06-kraken_'

    num_lines = sum(1 for line in open (file_txt))
    hits = (num_lines - 1) #to count the total number of hits

    lookupfile = open (file_txt, 'r')
    lines = lookupfile.readlines()
    parameters = lines[0].strip().split("\t")
    values_best_hit = lines[1].strip().split("\t")
    if num_lines >2:
        values_second_hit = lines[2].strip().split("\t")


    kmer_dict ={}


    for i in range (len(parameters)):

        kmer_dict[step + 'best_hit_' + parameters [i]] = values_best_hit [i]
        kmer_dict.update(Total_hits_06_kraken = hits)

        if num_lines >2:

            kmer_dict [step + 'second_hit_' + parameters [i]] = values_second_hit [i]

        else:

            kmer_dict [step + 'second_hit_' + parameters [i]] = ''

    return kmer_dict


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
        write.writerow(['sample_name', *header])
        for a, b in dictionary.items():
            write.writerow([a]+[b.get(i, '') for i in header])
    return


###################
### MAIN SCRIPT ###
###################


if __name__ == '__main__' :


    # Variables
    version = '01-kraken.py v 0.1.0.'  # Script version
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
    kmer_all = {}


    for sample in sample_list:

        file_name = os.path.join (path,sample, sample + '.brachen.sort')
        kmer_all[sample] = kraken_dictionary(file_name)
        print (file_name)

    print ('kraken_dictionary done')
    #print (kmer_all)


    # Save the dicctionary to binary file

    dictionary2bn (kmer_all, arguments.output_bn)

    print ('kraken_dictionary_bn done')

    # Convert the dictionary to csv file

    dictionary2csv (kmer_all, arguments.output_csv)

    print ('kraken_dictionary_csv done')
