# Genomic Tools and Registries

There are a growing number of (mostly open source) genomic analysis tools available.  In addition, there are genomic tool registries which help with discovery of such tools.  These include GATK, HAIL, ADAM, Bioconductor, IDSeq, VariantSpark and more.

## Tools and Pipelines

The general pattern for using bioinformatics tools in genomic analysis is to create a pipeline or workflow.  This is often done using a domain-specific language (DSL) for bioninformatics.  DSLs include WDL, CWL, Nextflow and GA (for Galaxy Project).  Workflows chain tools together and are run as jobs on scalable compute environments (cloud, HPC, etc...). A conceptual pipeline or workflow is shown below.  One or more tools are usually encapsulated in containers (docker, singularity or other types).  This is done for portability and reproducibility of research.

<img src="https://github.com/lynnlangit/TeamTeri/blob/master/Images/tools-pipeline.png" width=800>

## Genomics Registries

- Biocontainers - tool containers (images hosted on DockerHub, Quay.io or other public container registry)
- Dockstore - Genomic workflows - in CWL, NF or WDL (hosted in GitHub) and associated container-based tools
- Galaxy Toolshed - tools for Galaxy Project workflows (.ga files)
- nf-core - Nextflow workflows (.nf files)
- bioconda - Bioconda is a channel for the conda package manager specializing in bioinformatics software

## Blast 10 Ways

I wrote a short article on Medium using the `blast` tool, which demonstrates my approach to testing genomics tools - [link](https://medium.com/@lynnlangit/blast-10-ways-3db78f881059)