# DeepCell

From the Van Valen lab GitHub Repo Readme 

*"`deepcell-tf` is a deep learning library for **single-cell analysis of biological images**. It is written in Python and built using TensorFlow 2.  This library allows users to apply pre-existing models to imaging data as well as to develop new deep learning models for single-cell analysis. This library specializes in models for **cell segmentation (whole-cell and nuclear) in 2D & 3D images** as well as cell tracking in 2D time-lapse datasets. Read the documentation at deepcell.readthedocs.io."*
  
*"These models are applicable to data ranging from multiplexed images of tissues to dynamic live-cell imaging movies.  `deepcell-tf` is one of several resources created by the Van Valen lab to facilitate the development and application of new deep learning methods to biology."*

*"Other projects within our DeepCell ecosystem include the following:  "*
  *- **DeepCell Toolbox** for pre and post-processing the outputs of deep learning models "* 
  *- **DeepCell Tracking** for creating cell lineages with deep-learning-based tracking models "* 
  *- **DeepCell Kiosk** for deploying workflows on large datasets in the cloud  "*
  *- **DeepCell Label** for annotating high-dimensional biological images to use as training data  "*

## Test DeepCell on WebUI

Public test area --> https://deepcell.org/predict

## Install with Docker

Instructions from the Van Valen lab documenation --> [link](https://deepcell.readthedocs.io/en/latest/#install-with-docker)

```
# Start a GPU enabled container on one GPUs
docker run --gpus '"device=0"' -it --rm \
    -p 8888:8888 \
    -v $PWD/notebooks:/notebooks \
    -v $PWD/data:/data \
    vanvalenlab/deepcell-tf:latest-gpu
```

## Run on VertexAI Notebook

<img src="https://github.com/lynnlangit/TeamTeri/blob/master/Images/DeepCell-verify.png" width=800>

- Managed Jupyter Notebook
    - Use tensorflow runtime (screenshot above is an example)
    - Verify DeepCell
      ```
      import deepcell
      print("DeepCell version:", deepcell.__version__)
      ```
- User-managed Jupyter Notebook

## Run as a GCP Service

Recommended GCP architecture and image below on GKE cluster (from Van Valen lab documentation) - [link](https://deepcell-kiosk.readthedocs.io/en/master/#software-architecture)

<img src="https://raw.githubusercontent.com/vanvalenlab/kiosk-console/master/docs/images/Kiosk_Architecture.png" width=800>

## Use DeepCell for Cell Segmentation

Example from Van Valen lab (Jupyter notebook)--> [link](https://deepcell.readthedocs.io/en/latest/notebooks/Training-Segmentation.html)

