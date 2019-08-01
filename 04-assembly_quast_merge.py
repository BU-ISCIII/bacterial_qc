#!/usr/bin/env python3


import pandas as pd


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

    parser = argparse.ArgumentParser(prog = '03-preprocQC_fastqc_merge.py', formatter_class=argparse.RawDescriptionHelpFormatter, description= '03-preprocQC_fastqc_merge.py creates a unique csv file from  all the fastqc_csv files.')


    parser.add_argument('--path' ,'-p',required=True, help= 'Insert the path where are located the fastqc csv files')
    parser.add_argument('--output','-o', required=True, help='The output, merge of fastqc files')
    

    return parser.parse_args()



#################
### FUNCTIONS ###
#################


def quast_merge (path, csvfile):

    '''
    Description:
        Function to merge the fastqc csv files
    Input:
        path 
    Return:
        csv file with all the fastqc files (same columns (parameters) multiple rows (samples))
    '''

    all_files = glob.glob(path + "/*.csv")
    
    dataframes = [ pd.read_csv( f ) for f in all_files ] 
    
    df_fastqc_all = pd.concat([dataframes], axis=0, join='outer')
    df_fastqc_all.set_index('sample_name', inplace=True)
    df_fastqc_all.to_csv(csvfile)
    
    print (df_fastqc_all)
    #print ("df_fastqc_all file done")
    
    
    
###################
### MAIN SCRIPT ###
###################


if __name__ == '__main__' :


    # Variables
    version = '03-preprocQC_fastqc_merge v 0.1.0.'  # Script version
    
    # Create list
    arguments = check_arg(sys.argv[1:])
    extracted_list = fastqc_merge (arguments.path, arguments.output)
    
