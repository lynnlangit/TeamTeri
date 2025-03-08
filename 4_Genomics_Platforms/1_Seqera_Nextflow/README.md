# Nextflow (NF) & Seqera Cloud

<img src="https://github.com/lynnlangit/TeamTeri/blob/master/Images/nf-fundamentals.png" width=1000>

The Nextflow platform architecture is shown in the slide above.  [Seqera](https://seqera.io/) is a commercial company comprised of the core Nextflow committer team.

## About the Nextflow platform 
NF is built by Seqera Labs. NF pipelines can run on AWS, Azure, GCP and other environments
- start here - https://www.nextflow.io/index.html
- documentation - https://www.nextflow.io/docs/latest/index.html
- core concepts - https://www.nextflow.io/docs/latest/basic.html
- NF training - https://github.com/nextflow-io/training  

## Seqera and Nextflow

Seqera Labs plays a pivotal role in the development and support of the Nextflow platform. As the creators of Nextflow, Seqera is deeply committed to open-source development and actively contributes to the Nextflow community. Their expertise ensures that Nextflow remains at the forefront of workflow orchestration, enabling researchers and developers to build, run, and share data-driven analysis pipelines across a wide range of computing environments.

For more information about Seqera and their contributions to the Nextflow project, visit [Seqera's website](https://seqera.io/).

## Example Pipeline

Nextflow allows you to build, configure and run data-driven computational pipelines, an example is shown below.  Nextflow enables scalable and reproducible scientific workflows using software containers. The example diagram is for the [nf-core/eager](https://nf-co.re/eager) pipeline. This pipeline is a scalable and reproducible bioinformatics best-practise processing pipeline for genomic NGS sequencing data, with a focus on ancient DNA (aDNA) data. It is ideal for the (palaeo)genomic analysis of humans, animals, plants, microbes and even microbiomes

<kbd><img src="https://github.com/lynnlangit/TeamTeri/blob/master/Images/nf-pipe.png" width=1000></kbd>

---

## Cloud Based Execution

### AWS 

Conceptual architecture for running Nextflow pipeline on AWS is shown below.
- More detailed sample architecture for NF on AWS is shown below. 
- 7-min video concepts and quick demo --> https://www.youtube.com/watch?v=SYhDkUgcOXo&t=54s

<img src="https://github.com/lynnlangit/TeamTeri/blob/master/Images/nextflow-aws-batch.png" width=800>

## Execution Environments and Tools

Seqera Cloud is a commercial execution environment for Nextflow. Core architecture (from Seqera's documentation) is shown below.  
Seqera documentation is available at [link](https://docs.seqera.io/)

<kbd><img src="https://docs.seqera.io/assets/images/seqera_reference_architecture-11fa0ed3f5b9db1dadeb2f09252a53d6.png"></kbd>

## Example Workflows and Pipelines
- 📓  Example NF pipelines - [link](https://nf-co.re/pipelines)
- :octocat: Set of pipeline examples 'aweseome Nextflow' - [link](https://github.com/nextflow-io/awesome-nextflow)
- :octocat: Single-Cell Workflow(scFlow) pipeline from Imperial College of London
    - Orchestration of automated, scalable, and reproducible single-cell RNA sequencing analyses - [link](https://github.com/combiz/scFlow)
- 📘 Huge list of [Learn Nextflow links](https://www.nextflow.io/blog/2022/learn-nextflow-in-2022.html)
- :octocat: Nextflow pipeline 'gotchas' (examples) - [link](https://github.com/Midnighter/nextflow-gotchas)
