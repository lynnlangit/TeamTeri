# TeamTeri
Artifacts for patterns / tools for cloud-scaling cancer genomic data pipelines using... 
* **Public Cloud** : services from either GCP (Google Cloud Platform) or AWS (Amazon Web Services)
* **Bioinformatics** : frameworks, tools and libraries such as VariantSpark, Galaxy, ADAM and others
* **Practices** : industry patterns and practices for scalable data pipelines including serverless

## Understanding Cancer Genomic Data Analysis

![Cancer Sequencing Diagram](https://github.com/lynnlangit/TeamTeri/blob/master/Images/SequencingIllustrated.png)

As with any genome sequencing project, the reads must be assembled to form a representation of the chromosomes being sequenced. With cancer genomes, this is usually done by aligning the reads to the human reference genome.

Since even non-cancerous cells accumulate somatic mutations, it is necessary to compare sequence of the tumor to a matched normal tissue in order to discover which mutations are unique to the cancer. In some cancers, such as leukemia, it is not practical to match the cancer sample to a normal tissue, so a different non-cancerous tissue must be used.

It has been estimated that discovery of all somatic mutations in a tumor would require 30-fold sequencing coverage of the tumor genome and a matched normal tissue. By comparison, the original draft of the human genome had approximately 65-fold coverage.

A major goal of cancer genome sequencing is to identify driver mutations: genetic changes which increase the mutation rate in the cell, leading to more rapid tumor evolution and metastasis. It is difficult to determine driver mutations from DNA sequence alone; but drivers tend to be the most commonly shared mutations amongst tumors, cluster around known oncogenes, and are tend to be non-silent. Passenger mutations, which are not important in the progression of the disease,are randomly distributed throughout the genome. It has been estimated that the average tumor carries c.a. 80 somatic mutations, fewer than 15 of which are expected to be drivers.

A personal-genomics analysis requires further functional characterization of the detected mutant genes, and the development of a basic model of the origin and progression of the tumor. This analysis can be used to make pharmacological treatment recommendations. As of February 2012, this has only been done for patients clinical trials designed to assess the personal genomics approach to cancer treatment.

* **Main Link** : https://en.wikipedia.org/wiki/Cancer_genome_sequencing

* * *

## General Genomics Terms

* **Genomics** : refers to the study of the genome in contrast to genetics which refers to the study of genes and their roles in inheritance. Genomics is a discipline in genetics
* **DNA Sequencing** : is the process of determining the precise order of nucleotides within a DNA molecule. It includes any method or technology that is used to determine the order of the four bases—adenine, guanine, cytosine, and thymine—in a strand of DNA.
* **Genomics Analysis** : includes 3 parts - the sequencing of DNA, the assembly of that sequence to create a representation of the original chromosome, and the annotation and analysis of that representation.
* **Location** : a position on a chromosome. People have ~3 billion locations in their genetic code.
* **Variant** : a specific location on a chromosome where different people can have different genotypes or haplotypes. A rough estimate is that each person has 3 million variants.
* **Genotype** : a person's genetic code at a specific location, represented by 2 potentially different letters because each person generally has 2 instances of each location (i.e. G/A)
* **Haplotype** : half of a person's genetic code at a specific location, given with 1 letter (i.e. G)
* **Allele** : a specific haplotype, categorized into "reference allele" (i.e. G) and "alternate allele" (i.e. A)
* **Phenotype** : the way a specific allele is expressed for a particular characteristic (i.e. bbgg for blue eye color)
* **Biallelic** : a variant which is only represented by 2 different letters in our data (i.e. only G and A are present for all the people in our data, not T or C). Most variants are biallelic.

## Genomic Sequencing File Types

* .uBam or .FASTQ files - raw input files
    --unmapped BAM (from Illumina) base calls w/metadata
    --FASTQ with raw unmapped sequences without metadata
* .bam/.sam files - mapped reads
* .bed files - representations of genomic regions
* .vcf files - variant call format files

* * *

## Google Genomics API Terms

**Datasets** --A dataset is a logical grouping of genomic data and analysis associated with your cloud project. For example, a dataset might consist of aligned reads and variant calls from the 1000 Genomes project.

**Read group sets** — A read group set is a collection of reads, along with metadata about the sample, any processing that was performed, and the reference sequence.  In the simplest case, a read group set maps to a FASTQ or BAM file from a single sample, aligned with a particular alignment algorithm and parameters. When a BAM file contains reads from multiple biological samples, the reads are split up into multiple read group sets, one per sample. When multiple BAM files contain reads from the same sample, they must be merged into a single BAM file before import in order to create a single read group set.

**Reads** — Reads are nucleotide sequences generated by a DNA sequencing instrument, along with quality scores and metadata. Reads may be aligned to a reference sequence, or unaligned.

**References** — A reference is a canonical assembled DNA sequence, intended to act as a reference coordinate space for other genomic annotations. A single reference might represent the human chromosome 1 or mitochandrial DNA, for instance. A reference belongs to one or more reference sets.

**Reference sets** — A reference set is a set of references which typically comprise a reference assembly for a species, such as GRCh38 which is representative of the human genome. A reference set defines a common coordinate space for comparing reference-aligned experimental data. A reference set contains 1 or more references.

**Variants** — Variants are positions of genetic difference in a collection of call sets. Each variant identifies a position in a reference genome, a type of variant like SNP, insertion or deletion, the alternate allele, and the call sets that contain the variant. Variants may have standard names, like rs1234. Variants belong to a variant set.

**Variant sets** — A variant set is a collection of call sets and variants. It contains summary statistics of those contents. A variant set belongs to a dataset.

**Call set**s — A call set is a collection of variant calls, coming from a single sample using a particular variant calling algorithm and parameters.

**Operations** — Import and export of variants and reads, along with custom pipelines, are long-running operations. An operation resource maintains state, which can be queried for input and output details, along with execution status.

* * *

Explanation of NGS (next-generation sequencing - Illumina example) --
    https://github.com/ga4gh/schemas/issues/63

## NGS Diagram

![Next Generation Sequence Diagram](https://github.com/lynnlangit/TeamTeri/blob/master/Images/NGS-Workflow.png)

* * *