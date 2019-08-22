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

    parser = argparse.ArgumentParser(prog = '03-preprocQC .py', formatter_class=argparse.RawDescriptionHelpFormatter, description= '01-fastQC.py creates a csv file from fastqc.txt file')

    parser.add_argument('--path','-p', required=True, help='Insert path of fatsqc.txt file from 03-preprocQC folder like /home/user/Service_folder/ANALYSIS/03-preprocQC ') 
                        
                                    
    parser.add_argument('--output_bn','-b', required=True, help='The output in binary file')
    
    parser.add_argument('--output_csv','-c', required=True, help='The output in csv file')
  
    

    return parser.parse_args()



#################
### FUNCTIONS ###
#################


def fastqc_dict (file_txt, step):
    
    '''
    Description:
        Function to extract the relevant part of fastqc.txt file
    Input:
        fastqc.txt file
    Return:
        extracted_list
    '''
    
    qc_dict = {}
    header = False
    with open (file_txt, 'r') as fd:
        for line in fd:
            m = re.search ('END_MODULE',line)
            if m:
                break
            m = re.search('FastQC', line)
            if header:
                line = line.replace('\n','') 
                line = line.split('\t')
                qc_dict[step + '_post_' + line[0]] = line[1]
            if m:
                header = True
    
    return qc_dict


#################
### FUNCTIONS ###
#################


            
def fastqc_dictionary_bn (qc_dict, qc_dict_bn):
    
    '''

    Description:
        Function to create a binary file from a dictionary
    Input:
        kmer_dict from previus funtion
    Return:
        kmer_dict_bn
    '''


    pickle_out = open(qc_dict_bn,"wb")
    pickle.dump(qc_dict, pickle_out)
    pickle_out.close()

    return 


#################
### FUNCTIONS ###
#################


def fastqc_dictionary_csv (qc_all, qc_dict_csv, sample_list):

    '''

    Description:
        Function to create a csv from a dictionary
    Input:
        fastqc_dict from previus funtion
    Return:
        fastqc_dict_csv

    '''
    
    dic = qc_all
    outfile = qc_dict_csv
    header = sorted(set(i for b in map(dict.keys, dic.values()) for i in b))
    with open(outfile, 'w', newline="") as f:
        write = csv.writer(f)
        write.writerow(['sample_name'] + header)
        for a, b in dic.items():
            write.writerow([a]+[b.get(i, '') for i in header])


###################
### MAIN SCRIPT ###
###################


if __name__ == '__main__' :


    # Variables
    version = '01-fastQC v 0.1.0.'  # Script version
    arguments = check_arg(sys.argv[1:])
    
    # Create sample_id_list
    path = arguments.path
    sample_list = []
    tmp = os.listdir (path)
    for item in tmp:
        if os.path.isdir(os.path.join(path, item)):
            sample_list.append(item)

    #print ('sample_list done')
    print (sample_list)
        
    # Create a dictionary    
     
    fastq_all_post = {}
    dic_tmp = {}
    steps = ['R1_filtered_fastqc' , 'R2_filtered_fastqc']
    
    for sample in sample_list:
        fastq_all_post [sample] = {}
        for step in steps:
            file_name = os.path.join (path,sample,sample+'_'+step,"fastqc_data.txt")
            if os.path.exists(file_name)== False:
                #print(file_name, 'false')
                continue  
            else:
                #print('path exists' , os.path.exists(file_name))
                dic_tmp = fastqc_dict (file_name,step)
                if not fastq_all_post[sample]:
                    fastq_all_post[sample] = dic_tmp
                else:
                    #fastq_all_pre[sample] = {**fastq_all_pre[sample],**dic_tmp} 
                    fastq_all_post[sample].update(dic_tmp)
    
    #print ('fastq_all_post done')
    print (fastq_all_post)

    # Save the dicctionary to binary file
    
    fastqc_dictionary_bn (fastq_all_post, arguments.output_bn)
        
    print ('fastq_dictionary_bn done')
    
    # Convert the dictionary to csv file
    
    fastqc_dictionary_csv (fastq_all_post, arguments.output_csv, sample_list)
    
    print ('fastq_dictionary_csv done')
            
            