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

## AWS Template for DRAGEN w/FPGA


From the AWS docs --> 
- The DRAGEN Complete Suite* enables ultra-rapid analysis of NGS data for large data sets, such as whole genomes, exomes, and genes/panels
- This app uses the DRAGEN Platform and includes highly-optimized algorithms for mapping, aligning, sorting, duplicate marking, and haplotype variant calling
- The DRAGEN CS includes a host of pipelines including...
    - DRAGEN Germline Pipeline
    - DRAGEN Somatic Pipeline (T and T/N)
    - DRAGEN Copy Number Variant (CNV) Pipeline
    - DRAGEN RNA Gene Fusion, DRAGEN Joint Genotyping Pipeline
    - GATK Best Practices  
- The DRAGEN Germline and Somatic pipelines have greatly improved accuracy in calling SNPs and Indels compared to industry standard
- This app also supports Illumina NovaSeq BCL conversion, download/upload of data streaming, and compressed reference hash tables for a more seamless and efficient workflow
- Requires FPGA EC2 instances, from AWS Marketplace, costs ~ 20 USD/hr to run with CR template defaults - [link](https://aws.amazon.com/marketplace/pp/Illumina-Inc-DRAGEN-Complete-Suite/B07CZ3F5HY).  More info from the AWS Marketplace  

## Example DNA DRAGEN Pipeline

Shown below...  

<img src="https://github.com/lynnlangit/TeamTeri/blob/master/Images/dragen-dna.png" width=800>

## Example RNA DRAGEN Pipeline

Shown below...   

<img src="https://github.com/lynnlangit/TeamTeri/blob/master/Images/dragen-rna.png" width=800>

---

### AWS FPGA Dev Resources

<img src="https://github.com/lynnlangit/TeamTeri/blob/master/Images/fpga-arch.png" width=400 align=left>

- AWS QuickStart DRAGEN - [link](https://aws.amazon.com/quickstart/architecture/illumina-dragen/)
- AWS GitHub FPGA Dev Repo - [link](https://github.com/aws/aws-fpga)
- AWS FPGA Marketplace CF template - [link](https://aws.amazon.com/marketplace/pp/B06VVYBLZZ?qid=1611970635452&sr=0-8&ref_=brs_res_product_title)
- What is FPGA? - wikipedia [link](https://en.wikipedia.org/wiki/Field-programmable_gate_array)
- Image above from - [link](https://www.elprocus.com/fpga-architecture-and-applications/)

