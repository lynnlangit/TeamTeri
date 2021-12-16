# Nextflow (NF)

<img src="https://github.com/lynnlangit/TeamTeri/blob/master/Images/nf-pipe.png" width=1000>

Nextflow allows you to build, configure and run data-driven computational pipelines, an example is shown above.  Nextflow enables scalable and reproducible scientific workflows using software containers. The example diagram is for the [nf-core/eager](https://nf-co.re/eager) pipeline. This pipeline is a scalable and reproducible bioinformatics best-practise processing pipeline for genomic NGS sequencing data, with a focus on ancient DNA (aDNA) data. It is ideal for the (palaeo)genomic analysis of humans, animals, plants, microbes and even microbiomes

Nextflow allows the adaptation of pipelines written in the most common scripting languages.  Its fluent DSL simplifies the implementation and the deployment of complex parallel and reactive workflows on clouds and clusters.  The general pattern for deploying a Nextflow pipeline on a public cloud (VM batch) service is shown below.

<img src="https://github.com/lynnlangit/TeamTeri/blob/master/Images/nf-batch.png" width=800>

## About the Nextflow platform 
NF is built by Seqera Labs. An example architecture (running on AWS) is shown below. NF pipelines can run on AWS, Azure, GCP and other environments
- start here - https://www.nextflow.io/index.html
- documentation - https://www.nextflow.io/docs/latest/index.html
- core concepts - https://www.nextflow.io/docs/latest/basic.html

<img src="https://github.com/lynnlangit/TeamTeri/blob/master/Images/nextflow-aws-batch.png" width=800>

## Execution Environments and Tools
- Example NF pipelines - https://nf-co.re/pipelines
- Set of pipeline examples - https://github.com/nextflow-io/awesome-nextflow
- Tools / NFTower - https://help.tower.nf/getting-started/usage/ and see screen below 
  - Script with a nftower-cli tool - https://seqera.io/blog/announcing-the-nextflow-tower-cli
- Config runtime environments (include for AWS/Azure/GCP and more) for NF-Tower - https://help.tower.nf/compute-envs/overview/
  - NF on AWS Batch - https://docs.opendata.aws/genomics-workflows/orchestration/nextflow/nextflow-overview.html

<img src="https://github.com/lynnlangit/TeamTeri/blob/master/Images/nf-tower.png" width=800>


### Nextflow on GCP
- Patterns and info - [link on my repo 'gcp-for-bioinformatics'](https://github.com/lynnlangit/gcp-for-bioinformatics/blob/master/2_Virtual_Machines_%26_Docker_Containers/9a_Use_Nextflow_for_Pipelines.md)

