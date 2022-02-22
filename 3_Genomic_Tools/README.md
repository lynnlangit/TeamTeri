# Finding Genomic Tools 

There are a growing number of (mostly open source) genomic analysis tools available.  In addition, there are genomic tool **registries** which help with discovery of such tools.  These include GATK, HAIL, ADAM, Bioconductor, IDSeq, VariantSpark and more.  I highlight some recently released tools (listed below) as well.

- Tool which can be run in a browser! 
  - WebAssembly (open source) project named `biowasm` --> [link](https://biowasm.com/)
    - Includes samtools, bedtools, bowtie2, fastp, seq-align and more
- High-performance set of tools for research and commercial use
  - `fgbio`: tools for working with genomic and high throughput sequencing data --> [link](http://fulcrumgenomics.github.io/fgbio/tools/latest/)

## Tools and Pipelines

The general pattern for using bioinformatics tools in genomic analysis is to create a pipeline or workflow.  This is often done using a domain-specific language (DSL) for bioninformatics.  DSLs include WDL, CWL, Nextflow and GA (for Galaxy Project).  Workflows chain tools together and are run as jobs on scalable compute environments (cloud, HPC, etc...). A conceptual pipeline or workflow is shown below.  One or more tools are usually encapsulated in containers (docker, singularity or other types).  This is done for portability and reproducibility of research.

<img src="https://github.com/lynnlangit/TeamTeri/blob/master/Images/tools-pipeline.png" width=800>

## Genomic Tools - Registries

- [Genomic Visualizers](https://github.com/cmdcolin/awesome-genome-visualization) - huge list of visualization tools (companion website has screenshots!)
- [Biocontainers](https://biocontainers.pro/#/) - tool containers (images hosted on DockerHub, Quay.io or other public container registry)
- [Dockstore](https://dockstore.org/) - Genomic workflows - in CWL, NF or WDL (hosted in GitHub) and associated container-based tools
  - [Learn Dockstore](https://www.youtube.com/playlist?list=PL2uhATKMu4U_MxWFXCvu9WlASdJQgAevh) - series of short screencasts showing how to use the Dockstore registry
- [Galaxy Toolshed](https://toolshed.g2.bx.psu.edu/) - tools for Galaxy Project workflows (.ga files)
- [nf-core](https://nf-co.re/) - Nextflow workflows (.nf files)
- [bioconda](https://bioconda.github.io/) - Bioconda is a channel for the conda package manager specializing in bioinformatics software
- [bio-tools](https://bio.tools/t?page=1&q=gatk&sort=citationCount&ord=desc) - Example showing GATK tools by citation count and input/output and more (shown below)

<img src="https://github.com/lynnlangit/TeamTeri/blob/master/Images/bio-tools-registry.png" width=800>



## Blast 10 Ways

I wrote a short article on Medium using the `blast` tool, which demonstrates my approach to testing genomics tools - [link](https://medium.com/@lynnlangit/blast-10-ways-3db78f881059)

## Practical Advice

- 5 tips for better [bioinformatics software](https://www.youtube.com/watch?v=ujWnEMicotE) - useful video from Maria Nattestad
