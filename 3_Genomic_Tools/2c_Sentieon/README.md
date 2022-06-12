# Sentieon

Sentieon provides complete solutions for secondary DNA/RNA analysis for a variety of sequencing platforms, including short and long reads. Sentieon software **improves upon BWA, STAR, Minimap2, GATK, HaplotypeCaller, Mutect, and Mutect2 based pipelines** and is deployable on any generic-CPU-based computing system. 

Their [products](https://www.sentieon.com/products/) have been extensively tested and validated by customers, and have processed millions of samples totaling over 900 petabases of DNA. 

## Sentieon Analysis Pipelines & Tools

From their website...link above `products`

- **Alignment**
    - Sentieon BWA, STAR, Minimap2: identical match open source result with >2X speedup.
- **Germline SNV/INDEL Variant Calling**	
    - DNAseq: PrecisionFDA award-winning software. Matches GATK 3.3-4.1, and without downsampling. Results up to 10x faster and 100% consistent every time.
    - -DNAscope: Improved accuracy and genome characterization. Machine learning enhanced filtering producing top variant calling accuracy. Supports both short reads and PacBio HiFi long reads.
- **Somatic SNV/INDEL Variant Calling**	
    - TNseq: Matches MuTect, MuTect2 v3.8 - 4.1 without downsampling for higher accuracy and improved detections of low allelic fraction variants.
    - TNscope: Winner of ICGC-TCGA DREAM challenge. Improved accuracy, machine learning enhanced filtering. Supports molecular barcodes and unique molecular identifies.
- **Structural Variant Calling**	
    - Germline and somatic SV calling, including translocations, inversions, duplications and large INDELs.
- **Joint Calling**	
     - Supports large-cohort joint calling of over 200,000 WGS samples directly from gVCF and without intermediate steps.
- **BCL-FASTQ Tool**	
    - Sentieon's external library accelerates BCL to FASTQ conversion by 1.5 - 2x.
- **RNA Variant Calling**
    - Matches GATK RNAseq variant calling Best Practices.

----

## Using Sentieon Pieplines and Tools

- :octocat: Sentieon Github Organizational Repo --> [link](https://github.com/Sentieon)
- :octocat: Sentieon Github run-on-google-genomics Repo --> [link](https://github.com/Sentieon/sentieon-google-genomics)
- :book: Tutorial: run on Sentieon DNASeek pipeline on GCP LS API (Batch --> [link](https://cloud.google.com/life-sciences/docs/tutorials/sentieon)




