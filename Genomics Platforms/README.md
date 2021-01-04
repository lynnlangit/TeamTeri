# Genomics Platforms

Includes info about Galaxy Project, Terra.bio and Seven Bridges Genomics

## Workflow Languages

There are a number of DSLs (domain-specific languages) for genomics workflows.  These include the following:
- WDL - workflow definition language ('widdle') - open source, created at The Broad Institute - see my [`learn-wdl` open source course](https://github.com/openwdl/learn-wdl)
- CWL - common workflow language
- NF - Nextflow - see my ['Nextflow on GCP' summary](https://github.com/lynnlangit/gcp-for-bioinformatics/blob/master/2_Virtual_Machines_%26_Docker_Containers/9a_Use_Nextflow_for_Pipelines.md)
- GA - Galaxy Workflow Language - see the `Galaxy Project` folder in this Repo

## Workflow Patterns

Most workflows follow this pattern:
- Data Lake (shared file storage - local SAN or cloud buckets)
- Burstable compute cluster (HPC or cloud)
- Use of genomics workflow description language (see list above) - WDL, CWL, NF, GA
- Use of containers to encapsulate data analysis/processing tasks - docker or singularity containers, the latter for HPC environments