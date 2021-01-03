# GATK

![GATK Overview](https://github.com/lynnlangit/TeamTeri/blob/master/Images/GATK-1.png)

The open source [GATK (Genome Analysis Toolkit)](https://software.broadinstitute.org/gatk/) is the industry standard for identifying SNPs and indels in germline DNA and RNAseq data. Its scope is now expanding to include somatic variant calling tools, and to tackle copy number (CNV) and structural variation (SV). GATK is created and maintained by The Broad Institute.

----

## Using GATK Tools

Shown below is task-by-task usage for tools from the  GATK tools used in an example genomic analysis process  
![GATK Process](https://github.com/lynnlangit/TeamTeri/blob/master/Images/GATK-deep.png).

- RUN GATK with GCP Genomics (https://cloud.google.com/genomics/v1alpha2/gatk). 
- RUN Picard/GATK tools on GCP cloud-resident genomic data (http://googlegenomics.readthedocs.io/en/latest/use_cases/run_picard_and_gatk/index.html).
- UNDERSTAND Picard/GATK tools are command line utilities for genomic sequencing data processing that typically take BAM and other files as input and produce modified BAM files and can be downloaded from this link (http://broadinstitute.github.io/picard/)
- LEARN that these tools are frequently chained together into pipelines to perform step-by-step processing of the sequencing data all the way from unaligned sequencer output to variant calls. For more information see Broad best practices (https://software.broadinstitute.org/gatk/best-practices/).

----

## GATK running on Broad Institute Cloud Platforms

Alternatively, GATK tools are available running on GCP via the Broad Institute's 'FireCloud'(https://software.broadinstitute.org/firecloud/).  Firecloud is evolving to become the [Terra.bio](https://terra.bio/) interface which also runs on GCP.  Terra.bio architecture summary is shown in the screenshot below.  An example Firecloud screenshot is also shown below.

---

Terra.bio Architecture  
<img src="https://github.com/lynnlangit/TeamTeri/blob/master/Images/Terra-arch.png" width=800>  

---

Firecloud GATK WDL Workflows Example List
<img src="https://github.com/lynnlangit/TeamTeri/blob/master/Images/GATK-FireCloud.png" width=800>

## Genomics in the Cloud book

<img src="https://github.com/lynnlangit/TeamTeri/blob/master/Images/genomics-in-the-cloud.png" width=300>

- To learn more, I suggest reading the book ['Genomics in the Cloud'](https://www.amazon.com/Genomics-Cloud-GATK-Spark-Docker/dp/1491975199)
- One of the authors (Geraldine) wrote a book [chapter synopsis on twitter](https://twitter.com/VdaGeraldine/status/1263336914859560962?s=20)
- There is also an associated book club, run by [KT Picard](https://genomedad.com/2020/12/15/genomics-in-the-cloud-book-club/)
- The book club has a [YouTube channel](https://www.youtube.com/channel/UCtdwGKTSsRQZgAO6D79lSPA)
- The book club also has a [Slack channel](https://gitcbookclub.slack.com/).





