# [parse_assembly_quast.py](https://github.com/BU-ISCIII/bacterial_qc/blob/master/parse_assembly_quast.py)


## Description:

Python script to create a Dictionary and csv file with the [QUAST: Quality Assessment Tool for Genome Assemblies Metrics Report](http://quast.sourceforge.net/docs/manual.html#sec3.1)
data obtained from the quast_report.tsv files of [Outbreak_Brucellosis](https://github.com/sgonzalezbodi/Outbreak_Brucellosis).

The QUAST Summary Report generates some metrics for the file analysed (contig.fasta).

*   Total length (≥ x bp): The total number of bases in contigs of length ≥ x bp.
*   contigs: is the total number of contigs in the assembly.
*   Largest contig: The length of the longest contig in the assembly.
*   Total length: The total number of bases in the assembly.
*   GC (%): The total number of G and C nucleotides in the assembly, divided by the total length of the assembly.
*   N50: The length for which the collection of all contigs of that length or longer covers at least half an assembly.
*   NG50: The length for which the collection of all contigs of that length or longer covers at least half the reference genome.
*   N75 and NG75 are defined similarly to N50 but with 75 % instead of 50 %.
*   L50 (L75, LG50, LG75) is the number of contigs equal to or longer than N50 (N75, NG50, NG75). In other words, L50, for example, is the minimal number of contigsthat cover half the assembly.


## Input:

The following input argument is required:
 
*  -p pathList: path to the folder where there are all the report.tsv files we want to parse.
  
## Output files:
A dictionary converted to csv and binary file with the [QUAST: Quality Assessment Tool for Genome Assemblies Metrics Report](http://quast.sourceforge.net/docs/manual.html#sec3.1)
data obtained from the quast_report.tsv files:

```
-b /path/to/output_binary_file.bn
-c /path/to/output_csv_file.csv
``` 

Column data of the csv file:

* sample_id
* Total length 
* contigs
* Largest contig
* GC (%)
* N50 and NG50
* N75 and NG75 
* L50 (L75, LG50, LG75)

The output is obtained in a binary file and a csv file


For running in a local computer:

```
python3 /path/to/parse_assembly_quast.py 
-p /path/to/quast/ 
-c /path/to/RESULTS/dic_quast_stats_all.csv 
-b /path/to/RESULTS/dic_quast_stats_all.bn

```
