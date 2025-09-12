# Genomics LLMs and Models

This folder contains integrations with genomics models from Hugging Face Hub.

## Current Models

### Genereux-akotenou/genomics-tf-prediction
- **Type**: Keras tabular classification model
- **Downloads**: 18.4K
- **Task**: Genomics transcription factor prediction
- **Library**: TensorFlow/Keras

## Setup

1. Install required dependencies:
```bash
pip install -r requirements.txt
```

2. Run the model loader:
```bash
python genomics_model_loader.py
```

## Usage

```python
from genomics_model_loader import GenomicsModelLoader

# Initialize and load the model
loader = GenomicsModelLoader()
loader.download_model()
loader.load_model()

# Make predictions on your genomics data
predictions = loader.predict(your_genomics_data)
```

## Model Information

- **Model ID**: Genereux-akotenou/genomics-tf-prediction
- **Link**: https://huggingface.co/Genereux-akotenou/genomics-tf-prediction
- **Task**: Tabular classification for genomics data
- **Framework**: Keras/TensorFlow

## Integration with Other Sequencing Tools

This model can be integrated with data from:
- `../1_Illumina/` - Illumina sequencing data
- `../2_PacBio/` - PacBio long-read data
- `../3_DNANudge/` - DNANudge analysis results
- `../4_Ambrygen/` - Ambrygen diagnostic data

## Next Steps

1. Prepare your genomics data in the format expected by the model
2. Use the prediction results for downstream analysis
3. Integrate with your existing sequencing workflows