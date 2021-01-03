# Genomics Platforms

Includes info about Galaxy Project, Terra.bio and Seven Bridges Genomics

## Workflow Languages

There are a number of DSLs (domain-specific languages) for genomics workflows.  These include the following:
- WDL - workflow definition language - open source, created at The Broad Institute
- CWL - common workflow language
- NF - Nextflow
- GA - Galaxy Workflow Language

## Workflow Patterns

Most workflows follow this pattern:
- Data Lake (shared file storage - local SAN or cloud buckets)
- Burstable compute cluster (HPC or cloud)
- Use of genomics workflow description language (see list above)
- Use of containers to encapsulate data analysis/processing tasks