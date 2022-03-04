# Genomics Platforms

Includes info about Galaxy Project, Terra.bio, Nextflow and Seven Bridges Genomics. This represents a small subset of the available platforms.  Some platforms are free (for research), others are commercial and have associated costs.  Still other platforms have a 'free tier' (running on public cloud) and then a 'you-pay-for-it' tier, usually based on the size of the data you need to analyze.  

Platforms are designed to run **workflows** (which are sometimes called pipeliens) for genomic data anaylsis.  Workflows consist of a series of processing steps or **tasks**.  These tasks can be written via scripts (for example in R or Python) or can be executed using genomic libraries or toolkits, such as GATK (Genome Analysis Toolkit) from The Broad Institute.

Each time a workflow is run it generates a **job execution**.  Individual jobs can be tracked and monitored for accuracy, performance and runtime.

## Workflow Patterns

Most workflows follow this pattern (summarized in the diagram below for AWS):
- **Data Lake** (shared file storage - local SAN or cloud buckets)
- Burstable **compute cluster** (HPC or cloud) - use VMs and/or container clusters on the cloud
- Use of **genomics workflow description language** (see list above) - WDL, CWL, NF, GA
- Use of **containers to encapsulate data analysis tasks/tools** - docker or singularity containers, the latter for HPC environments
- Use of **libraries AND job controllers** to manage cluster resources (CPU, RAM) - cloud libraries include AWS Batch, Azure Batch, GCP Life Sciences

<img src="https://github.com/lynnlangit/TeamTeri/blob/master/Images/lake-pattern.png" width=800>

The diagram above shows a workflow one possible example. It uses cloud vendor AWS (VM controller `AWS Batch` service, workflow language / job controller `cromwell service` (for `WDL language`) and genomic analysis toolset `GATK`.

## Workflow Languages

There are a number of DSLs (domain-specific languages) for genomics workflows.  These include the following:
- **WDL** - workflow definition language ('widdle') - open source, created at The Broad Institute - see my [`learn-wdl` open source course](https://github.com/openwdl/learn-wdl) usally runs with the `cromwell` service, but can use other services, `miniwdl` and others.
- **CWL** - common workflow language
- **NF** - Nextflow - see my ['Nextflow on GCP' summary](https://github.com/lynnlangit/gcp-for-bioinformatics/blob/master/2_Virtual_Machines_%26_Docker_Containers/9a_Use_Nextflow_for_Pipelines.md)
- **GA** - Galaxy Workflow Language - see the `Galaxy Project` folder in this Repo
