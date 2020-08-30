# [mlst_report.py](https://github.com/BU-ISCIII/bacterial_qc/blob/master/mlst_report.py)


## Description:

Python script to create a Dictionary and csv file with the [ARIBA: A tool that identifies antibiotic resistance genes by running local assemblies. It can also be used for MLST calling](https://github.com/sanger-pathogens/ariba) data obtained from the ariba_report.tsv files of [Outbreak_Brucellosis](https://github.com/sgonzalezbodi/Outbreak_Brucellosis).

The meaning of the columns in mlst_report.tsv is as follows:

*   gene: the name of the gene
*   allele: the allele called
*   cov: percent of the gene that was assembled
*   pc: percent identity between the gene and assembly
*   ctgs: number of contigs in the assembly
*   depth: mean read depth of the contig(s)
*   hetmin: minimum(max allele depth as a percent of total depth), across all identified heterozygous SNPs. e.g. for the example below where the hets column is 30,10.25,10,5, this would be 100 * min(30/(30+10), 25/(25+10+5)) = 62.5.
*   hets: a list of the heterozygous SNP depths. For example 30,10.25,10,5 corresponds to two heterozygous SNPs, the first with read depths 30 and 10, and the second with depths 25, 10, and 5.

## Input:

The following input argument is required:

``` 
-p pathList: path to the folder where there are all the report.tsv files we want to parse.

```  

## Output files:

A dictionary converted to csv and binary file with the  [ARIBA: Antimicrobial Resistance Identification By Assembly Report](https://github.com/sanger-pathogens/ariba)data obtained from the ariba_report.tsv files:

```
-b /path/to/output_binary_file.bn
-c /path/to/output_csv_file.csv
``` 

Column data of the csv file is a summary of the allele calls and identified sequence type in each sample. 

* sample_id
* Housekeeping gene (allele)

The output is obtained in a binary file and a csv file


For running in a local computer:

```
python3 /path/to/report_mlst.py 
-p /path/to/ariba/MLST/ 
-c /path/to/RESULTS/dic_ariba_MLST_all.csv 
-b /path/to/RESULTS/dic_ariba_MLST_all.bn

```
