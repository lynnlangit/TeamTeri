# Genomics Platforms

Includes info about Galaxy Project, Terra.bio and Seven Bridges Genomics. This represents a small subset of the available platforms.  Some platforms are free (for research), others are commercial and have associated costs.  Still other platforms have a 'free tier' (running on public cloud) and then a 'you-pay-for-it' tier, usually based on the size of the data you need to analyze.
## Workflow Patterns

Most workflows follow this pattern (summarized in the diagram below):
- **Data Lake** (shared file storage - local SAN or cloud buckets)
- Burstable **compute cluster** (HPC or cloud) - use VMs and/or container clusters on the cloud
- Use of **genomics workflow description language** (see list above) - WDL, CWL, NF, GA
- Use of **containers to encapsulate data analysis tasks/tools** - docker or singularity containers, the latter for HPC environments
- Use of **libraries AND job controllers** to manage cluster resources (CPU, RAM) - cloud libraries include AWS Batch, Azure Batch, GCP Life Sciences

<img src="https://github.com/lynnlangit/TeamTeri/blob/master/Images/analysis-toolkit.png" width=800>

## Workflow Languages

There are a number of DSLs (domain-specific languages) for genomics workflows.  These include the following:
- **WDL** - workflow definition language ('widdle') - open source, created at The Broad Institute - see my [`learn-wdl` open source course](https://github.com/openwdl/learn-wdl)
- **CWL** - common workflow language
- **NF** - Nextflow - see my ['Nextflow on GCP' summary](https://github.com/lynnlangit/gcp-for-bioinformatics/blob/master/2_Virtual_Machines_%26_Docker_Containers/9a_Use_Nextflow_for_Pipelines.md)
- **GA** - Galaxy Workflow Language - see the `Galaxy Project` folder in this Repo