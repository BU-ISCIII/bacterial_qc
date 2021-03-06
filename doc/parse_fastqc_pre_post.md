# [parse_fastqc_pre_post](https://github.com/BU-ISCIII/bacterial_qc/blob/master/parse_fastqc_all.py)


## Description:
Python script to create a Dictionary and csv file with the [FastQC Basic Statistics](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/Help/3%20Analysis%20Modules/1%20Basic%20Statistics.html) data obtained from the fastqc_data.txt files of [Outbreak_Brucellosis](https://github.com/sgonzalezbodi/Outbreak_Brucellosis).

The FastQC Basic Statistics module generates some simple composition statistics for the file analysed.

*   Filename: The original filename of the file which was analysed
*   File type: Says whether the file appeared to contain actual base calls or colorspace data which had to be converted to base calls
*   Encoding: Says which ASCII encoding of quality values was found in this file.
*   Total Sequences: A count of the total number of sequences processed. 
*   Filtered Sequences: If running in Casava mode sequences flagged to be filtered will be removed from all analyses. The number of such sequences removed will be reported here. The total sequences count above will not include these filtered sequences and will the number of sequences actually used for the rest of the analysis.
*   Sequence Length: Provides the length of the shortest and longest sequence in the set. If all sequences are the same length only one value is reported.
*   %GC: The overall %GC of all bases in all sequences



## Input:
The following input arguments are required:
 
*  -p pathList: path to the folder where there are all the fastqc_data.txt files we want to parse
*  -s argument-step: from fastqc_data.txt check the line of filename and add the end of the string which has the information of the step(pre-trimmomatic or post-trimmomatic) and the forward (R1) and reverse (R2) reads as an example:"_R1.fastq.gz", "_R2.fastq.gz","_R1_filtered.fastq.gz","_R2_filtered.fastq.gz"
* -t argument-tag : our nomenclature to define the step and the reads that has to combine with the argument_step (pre_R1","pre_R2", "post_R1","post_R2")


``` 
-p /path/to/fastqc-folder/ 
-s _R1.fastq.gz _R2.fastq.gz .trimmed_R1.fastq .trimmed_R2.fastq 
-t pre_R1 pre_R2 post_R1 post_R2 
```
  
## Output files:
A dictionary converted to csv and binary file with the [FastQC Basic Statistics](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/Help/3%20Analysis%20Modules/1%20Basic%20Statistics.html) of the fastq files:

```
-b /path/to/output_binary_file.bn
-c /path/to/output_csv_file.csv
``` 


Column data of the csv file:

* sample
* Filename
* File type
* Encoding
* Total Sequences
* Sequence length
* Sequences flagged as poor quality
* %GC

The output is obtained in a binary file and a csv file


## Example

For running in a local computer:

```
python3 /path/to/parse_fastqc_all.py 
-p /path/to/fastqc/ 
-s _R1.fastq.gz _R2.fastq.gz .trimmed_R1.fastq .trimmed_R2.fastq 
-t pre_R1 pre_R2 post_R1 post_R2 
-c /path/to/RESULTS/dic_fastqc_stats_all.csv 
-b /path/to/RESULTS/dic_fastqc_stats_all.bn

```
