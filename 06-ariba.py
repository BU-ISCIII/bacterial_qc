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

    parser = argparse.ArgumentParser(prog = '06-ariba.py', formatter_class=argparse.RawDescriptionHelpFormatter, description= '06-ariba.py creates a csv file from results.txt file')

    parser.add_argument('--input' ,'-i',required=True, help='Insert report.tsv from path:Service_folder /home/user/Service_folder/ANALYSIS/06-ariba/sumaryl/out.summarycard.csv ')
    
    parser.add_argument('--database','-d', required=True, help='The database used (card, megares or srst2')
                     
    parser.add_argument('--output_bn','-b', required=True, help='The output in binary file')
    
    parser.add_argument('--output_csv','-c', required=True, help='The output in csv file')
  
    

    return parser.parse_args()



#################
### FUNCTIONS ###
#################


def ariba_dictionary_card (file_csv):
    
    '''
    Description:
        Function to extract the relevant part of out.summarycard.csv file
    Input:
        out.summarycard.csv file
    Return:
        dictionary
    '''
    
    parameter = 'resistance_genes_car'
    with open(file_csv) as csvfile:
        data = list (csv.reader(csvfile))
        genes_list = {}
        
        for row in range (len(data)):
            if row == 0:
                header = data[row]
            else:
                genes = []
                for i in range (len (data [row])):
                    if  data[row][i] == 'yes':
                        gene_resis = 'yes'
                        genes.append(header[i])
                    else:
                        gene_resis = 'no'

                tmp = os.path.basename (data[row][0])
                sample = re.search(r"(.*?(?=cardreport.tsv))", tmp).group(0)

                genes_list [sample] = {}
                genes_list [sample] [parameter] = genes
                genes_list[sample].update(resistance_card = gene_resis )



    return (genes_list)

#################
### FUNCTIONS ###
#################


def ariba_dictionary_megares (file_csv):
    
    '''
    Description:
        Function to extract the relevant part of out.summarymegares.csv file
    Input:
        out.summarydatbase.csv file
    Return:
        dictionary
    '''
    
    parameter = 'resistance_genes_megares'
    with open(file_csv) as csvfile:
        data = list (csv.reader(csvfile))
        genes_list = {}
        genes_list [sample] = {}
        for row in range (len(data)):
            if row == 0:
                header = data[row]
            else:
                genes = []
                for i in range (len (data [row])):
                    if  data[row][i] == 'yes':
                        gene_resis = 'yes'
                        genes.append(header[i])
                    else:
                        gene_resis = 'no'

                tmp = os.path.basename (data[row][0])
                sample = re.search(r"(.*?(?=megaresreport.tsv))", tmp).group(0)

                genes_list [sample] = {}
                genes_list [sample] [parameter] = genes
                genes_list[sample].update(resistance_megares = gene_resis )



    return (genes_list)

    
#################
### FUNCTIONS ###
#################


def ariba_dictionary_csv (genes_list, csvfile):
    
    '''
    
    Description:
        Function to create a csv from a dictionary
    Input:
        genes_list from previus funtion
    Return:
        card_dict_csv
        
   '''
    
    dic     = genes_list #Nested dictionary 
    parameters = sorted (list(list (dic.values())[0].keys())) 

    with open(csvfile, "w") as f:
        w = csv.writer( f )
        w.writerow(['sample_name'] + parameters)

        for sample in dic.keys():
            w.writerow([sample] + [dic[sample][parameter] for parameter in parameters])


            
#################
### FUNCTIONS ###
#################


def ariba_dictionary_bn (genes_list, ariba_dict_bn):
    
    '''

    Description:
        Function to create a binary file from a dictionary
    Input:
        genes_list from previus funtion
    Return:
       ariba_dict_bn
    '''


    pickle_out = open(ariba_dict_bn,"wb")
    pickle.dump(genes_list, pickle_out)
    pickle_out.close()

    return     

###################
### MAIN SCRIPT ###
###################



if __name__ == '__main__' :


    # Variables
    version = '06-ariba v 0.1.0.'  # Script version
    arguments = check_arg(sys.argv[1:])
    
    
    # Create a dictionary
    
    #if arguments.database == 'card':
    ariba_dict = ariba_dictionary_card (arguments.input)
    print ('ariba_dict_card done')
    print (ariba_dict)
    
    #if arguments.database == 'megares':
        #ariba_dict = ariba_dictionary_megares (arguments.input)
    
        #print ('ariba_dict_megares done')
        #print (ariba_dict)
    

    #Convert the dictionary to csv file
    
    ariba_dictionary_csv (ariba_dict, arguments.output_csv)
    
    print ('ariba_dictionary_csv done')
   
  
         
    # Save the dicctionary to binary file
    
    ariba_dictionary_bn (ariba_dict, arguments.output_bn)
        
    print ('ariba_dictionary_bn done')
            