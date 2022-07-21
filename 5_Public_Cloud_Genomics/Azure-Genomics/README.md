# Azure Genomics

For more - see - https://azure.microsoft.com/en-us/services/genomics/  

NOTE: You may need to use a 'pay-as-you-go' Azure account [purchase option](https://azure.microsoft.com/en-us/pricing/purchase-options/) to be able to run genomic examples (rather than a free trial account).  The reason for this is that the compute CPU/GPU quota in [free trial Azure accounts](https://azure.microsoft.com/en-us/free/free-account-faq/) is quite limited.

## Genomic Datasets on Azure

- Azure Open Genomics Datasets - https://azure.microsoft.com/en-us/services/open-datasets/catalog/genomics-data-lake/

## About Microsoft Genomics

To Azure Batch and standard tools (such as GATK), Microsoft adds their genomics client (`msgen`) for running genomics workloads.  

- The Microsoft Genomics client (`msgen`) is a Python front-end to the web service, architecture shown below
- It can beinstalled like a standard Python package, on Windows or Linux via `pip install msgen`
- For each genome sample that you want to process, you create a configuration file containing all the parameters

<img src="https://github.com/lynnlangit/TeamTeri/blob/master/Images/msft-genomics.png" width=600>

---

## Genomics Workflow Languages and Azure Batch

### Nextflow

- 📄 Nextflow on Azure Batch - [link](https://www.nextflow.io/blog/2021/introducing-nextflow-for-azure-batch.html)

### WDL/Cromwell/Terra (and GATK)

- 📘 WDL/Cromwell on Azure Batch - [link](https://lynnlangit.medium.com/azure-for-genomic-scale-workloads-ad3c989a3d0b)
- :octocat: cromwell-on-azure source code - [link](https://github.com/microsoft/CromwellOnAzure)
- 📢 Terra.bio runnable on Azure (announced in 2021) - [link](https://terra.bio/exciting-new-horizon-for-terra-with-microsoft/)
- 📄 DRAGEN (requires FPGA) on Azure Batch using Illumina Bio-IT Platform for genomic analysis - [link](https://support-docs.illumina.com/SW/Dragen_MultiCloud/Content/SW/DRAGEN/AzureBatch.htm)

### FIHR Server

- 📘 FHIR Server and Azure Synapse - [link](https://techcommunity.microsoft.com/t5/healthcare-and-life-sciences/combine-and-explore-fhir-server-and-genomics-data-in-azure/ba-p/3298335)

