# Illumina DRAGEN

From the Illumina documentation - [link](https://support.illumina.com/content/dam/illumina-support/documents/documentation/software_documentation/dragen-bio-it/Illumina-DRAGEN-Bio-IT-Platform-User-Guide-1000000141465-00.pdf)

The Illumina DRAGEN™ Bio-IT Platform is based on the highly reconfigurable DRAGEN Bio-IT Processor,
which is integrated on a Field Programmable Gate Array (FPGA) card and is available in a preconfigured
server that can be seamlessly integrated into bioinformatics workflows. The platform can be loaded
with highly optimized algorithms for many different NGS secondary analysis pipelines, including the
following:  

• Whole genome
• Exome
• RNA-Seq
• Methylome
• Cancer

All interaction is accomplished via DRAGEN software that runs on the host server and manages all
communication with the DRAGEN board.

## AWS Template for DRAGEN

Requires FPGA EC2 instances, from AWS Marketplace, costs ~ 20 USD/hr to run with CR template defaults - [link](https://aws.amazon.com/marketplace/pp/Illumina-Inc-DRAGEN-Complete-Suite/B07CZ3F5HY).  More info from the AWS Marketplace  

"The DRAGEN Complete Suite* enables ultra-rapid analysis of Next Generation Sequencing (NGS) data for large data sets, such as whole genomes, exomes, and genes/panels. This application uses the DRAGEN Platform and includes highly-optimized algorithms for mapping, aligning, sorting, duplicate marking, and haplotype variant calling. The DRAGEN CS includes a host of pipelines including our DRAGEN Germline Pipeline, DRAGEN Somatic Pipeline (T and T/N), DRAGEN Copy Number Variant (CNV) Pipeline, DRAGEN RNA Gene Fusion, DRAGEN Joint Genotyping Pipeline, and GATK Best Practices. The DRAGEN Germline and Somatic pipelines have greatly improved accuracy in calling SNPs and Indels compared to industry standard. This app also supports Illumina NovaSeq BCL conversion, download/upload of data streaming, and compressed reference hash tables for a more seamless and efficient workflow."

## Exaple DNA DRAGEN Pipeline

Shown below...  

<img src="https://github.com/lynnlangit/TeamTeri/blob/master/Images/dragen-dna.png" width=800>

## Exaple RNA DRAGEN Pipeline

Shown below...   

<img src="https://github.com/lynnlangit/TeamTeri/blob/master/Images/dragen-rna.png" width=800>