# Genomic-Epidemiology-of-SARS-Cov-2-in-Nepal
1. Install minicond3

wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh # wget is used download from the internet using url

bash ~/Miniconda3-latest-Linux-x86_64.sh #bash command is used to run bash script 


2. Dependencies for covseq were installed prior to cloning it from github

Python Dependencies: 
click
biopython
hashlib
pandas [>=1.0.3]
matplotlib
seaborn
dateutil
werkzeug


bcftools and htslib were build from the source. To build them, youtube tutorial was preferred.
https://youtu.be/EJGz3yryrPo?si=umXzdbm_SNoF2r-Y

3.covseq github repo was cloned.
github clone "https://github.com/boxiangliu/covseq"

4.Move into covseq directory 
cd covseq

5.annotation.py script was run for each parsed multifasta file 
python3 annotation/annotation.py --fasta  filename.fasta --out /home/himanshu/covseq/processed/covseq/Annotations


