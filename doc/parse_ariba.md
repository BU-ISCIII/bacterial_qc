# [parse_ariba.py](https://github.com/BU-ISCIII/bacterial_qc/blob/master/parse_ariba.py)


## Description:

Python script to create a Dictionary and csv file with the [ARIBA: Antimicrobial Resistance Identification By Assembly Report](https://github.com/sanger-pathogens/ariba) data obtained from the ariba_report.tsv files of [Outbreak_Brucellosis](https://github.com/sgonzalezbodi/Outbreak_Brucellosis).

The meaning of the columns in report.tsv is as follows:

*   1. ariba_ref_name	ariba name of reference sequence chosen from cluster (needs to rename to stop some tools breaking)
*   2. ref_name	original name of reference sequence chosen from cluster, before renaming
*   3. gene	1=gene, 0=non-coding (same as metadata column 2)
*   . var_only	1=variant only, 0=presence/absence (same as metadata column 3)
*   5. flag	cluster flag
*   6. reads	number of reads in this cluster
*   7. cluster	name of cluster
*   8. ref_len	 length of reference sequence
*   9. ref_base_assembled	number of reference nucleotides assembled by this contig
*   10. pc_ident	%identity between reference sequence and contig
*   11. ctg	name of contig matching reference
*   12. ctg_len	length of contig
*   13. ctg_cov	mean mapped read depth of this contig
*   14. known_var	is this a known SNP from reference metadata? 1 or 0
*   15. var_type	The type of variant. Currently only SNP supported
*   16. var_seq_type	Variant sequence type. if known_var=1, n or p for nucleotide or protein
*   17. known_var_change	if known_var=1, the wild/variant change, eg I42L
*   18. has_known_var	if known_var=1, 1 or 0 for whether or not the assembly has the variant
*   19. ref_ctg_change	amino acid or nucleotide change between reference and contig, eg I42L
*   20. ref_ctg_effect	effect of change between reference and contig, eg SYS, NONSYN (amino acid changes only)
*   21. ref_start	start position of variant in reference
*   22. ref_end	end position of variant in reference
*   23. ref_nt	nucleotide(s) in reference at variant position
*   24. ctg_start	start position of variant in contig
*   25. ctg_end	end position of variant in contig
*   26. ctg_nt	nucleotide(s) in contig at variant position
*   27. smtls_total_depth	 total read depth at variant start position in contig, reported by mpileup
*   28. smtls_nts	nucleotides on contig, as reported by mpileup. The first is the contig nucleotide
*   29. smtls_nts_depth	depths on contig, as reported by mpileup. One number per nucleotide in the previous column
*   30. var_description	description of variant from reference metdata
*   31. free_text	other free text about reference sequence, from reference metadata

## Input:

The following input argument is required:

``` 
-p pathList: path to the folder where there are all the report.tsv files we want to parse.
-d the database used of AMR (card, megares or srst2_argannot)
```  

## Output files:

A dictionary converted to csv and binary file with the  [ARIBA: Antimicrobial Resistance Identification By Assembly Report](https://github.com/sanger-pathogens/ariba)data obtained from the ariba_report.tsv files:

```
-b /path/to/output_binary_file.bn
-c /path/to/output_csv_file.csv
``` 

Column data of the csv file:

* sample_id
* Resistence gene (1=yes/0=No)

The output is obtained in a binary file and a csv file


For running in a local computer:

```
python3 /path/to/parse_ariba.py 
-p /path/to/ariba/ 
-c /path/to/RESULTS/dic_ariba_AMR_all.csv 
-b /path/to/RESULTS/dic_ariba_AMR_all.bn

```
