# HAIL-IS on Apache Spark

[Hail](https://hail.is) is an [open-source](https://github.com/hail-is/hail), scalable framework for exploring and analyzing genetic data from The Broad Instiute. Starting from sequencing or microarray data in VCF and other formats, Hail can, for example:

## HAIL Features

* generate variant annotations like call rate, Hardy-Weinberg equilibrium p-value, 
and population-specific allele count
* generate sample annotations like mean depth, imputed sex, and TiTv ratio
* load variant and sample annotations from text tables, JSON, VCF, VEP, and locus interval files
* produce new annotations computed from existing annotations and the genotypes, and use these to filter samples, variants, and genotypes
* compute sample scores and variant loadings using principal compenent analysis, or project your cohort onto ancestry coordinates of reference datasets
* perform association analyses with phenotypes and covariates using linear and logistic regression

All this functionality is backed by distributed algorithms built on top of Apache Spark to efficiently analyze gigabyte-scale data on a laptop or terabyte-scale data on an on-prem cluster or in the cloud.

## Docs/Tutorials

- [Using HAIL on GCP / Cloud Dataproc](https://hail.is/docs/0.2/hail_on_the_cloud.html)
- [HAIL on AWS](https://aws-quickstart.github.io/quickstart-hail/)
- [Hail Tables cheat sheet](https://hail.is/docs/0.2/_static/cheatsheets/hail_tables_cheat_sheet.pdf)
- [Hail MATRIX Tables cheat sheet](https://hail.is/docs/0.2/_static/cheatsheets/hail_matrix_tables_cheat_sheet.pdf)