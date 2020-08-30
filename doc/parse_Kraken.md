# [parse_Kraken.py](https://github.com/BU-ISCIII/bacterial_qc/blob/master/parse_Kraken.py)


## Description:

Python script to create a Dictionary and csv file with the [KRAKEN: Taxonomic Sequence Classification System](http://ccb.jhu.edu/software/kraken/) data obtained from the KRAKEN_report.tsv files of [Outbreak_Brucellosis](https://github.com/sgonzalezbodi/Outbreak_Brucellosis).

The output of kraken-report is tab-delimited, with one line per taxon. The fields of the output, from left-to-right, are as follows:

*   Percentage of reads covered by the clade rooted at this taxon
*   Number of reads covered by the clade rooted at this taxon
*   Number of reads assigned directly to this taxon
*   A rank code, indicating (U)nclassified, (D)omain, (K)ingdom, (P)hylum, (C)lass, (O)rder, (F)amily, (G)enus, or (S)pecies. All other ranks are simply '-'.
*   NCBI taxonomy ID
*   indented scientific name

## Input:

The following input argument is required:
 
*  -p pathList: path to the folder where there are all the report.tsv files we want to parse.
  
## Output files:
A dictionary converted to csv and binary file with the [KRAKEN: Taxonomic Sequence Classification System](http://ccb.jhu.edu/software/kraken/)data obtained from the KRAKEN_report.tsv files:

```
-b /path/to/output_binary_file.bn
-c /path/to/output_csv_file.csv
``` 

Column data of the csv file from the first a second hit of each sample and the last column is the total number of hits of each sample:

* sample_id
* taxonomy_id     
* taxonomy_lvl    
* kraken_assigned_reads   
* added_reads     
* new_est_reads   
* fraction_total_reads
* total_number_hits

The output is obtained in a binary file and a csv file

For running in a local computer:

```
python3 /path/to/parse_kraken.py 
-p /path/to/kraken/ 
-c /path/to/RESULTS/dic_kraken_stats_all.csv 
-b /path/to/RESULTS/dic_kraken_stats_all.bn

```
