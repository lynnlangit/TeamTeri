# Tips for DRAGEN

## Build a hashtable reference

DRAGEN requires a proprietary hashtable reference. Copy your own FASTA reference file onto the instance and put it in /staging, or get the hg19 FASTA files from UCSC and concatenate them into a single hg19.fa file using these instructions:

````
mkdir /staging/hg19fa
cd /staging/hg19fa
wget hgdownload.cse.ucsc.edu/goldenPath/hg19/bigZips/chromFa.tar.gz
tar -zxvf chromFa.tar.gz
cat chr*.fa > hg19.fa
````
