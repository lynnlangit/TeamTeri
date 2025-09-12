"""
Genomics Model Loader for Hugging Face Models
Load and use the most popular genomics model from Hugging Face Hub
"""

import os
import numpy as np
import pandas as pd
from huggingface_hub import hf_hub_download
import tensorflow as tf
from typing import Optional, Union

class GenomicsModelLoader:
    """
    Loader for the Genereux-akotenou/genomics-tf-prediction model
    This is a Keras model for tabular classification in genomics
    """
    
    def __init__(self, model_id: str = "Genereux-akotenou/genomics-tf-prediction"):
        self.model_id = model_id
        self.model = None
        self.model_path = None
        
    def download_model(self, cache_dir: Optional[str] = None) -> str:
        """
        Download the model from Hugging Face Hub
        
        Args:
            cache_dir: Directory to cache the model (optional)
            
        Returns:
            Path to the downloaded model
        """
        try:
            print(f"Downloading model from {self.model_id}...")
            
            # Download the main model file
            self.model_path = hf_hub_download(
                repo_id=self.model_id,
                filename="model.h5",  # Keras models typically use .h5 format
                cache_dir=cache_dir
            )
            
            print(f"Model downloaded successfully to: {self.model_path}")
            return self.model_path
            
        except Exception as e:
            print(f"Error downloading model: {e}")
            # Try alternative filename patterns
            try:
                self.model_path = hf_hub_download(
                    repo_id=self.model_id,
                    filename="saved_model.pb",
                    cache_dir=cache_dir
                )
                return self.model_path
            except:
                print("Could not find model file. Please check the repository structure.")
                return None
    
    def load_model(self) -> bool:
        """
        Load the downloaded model
        
        Returns:
            True if successful, False otherwise
        """
        if not self.model_path:
            print("No model path available. Please download the model first.")
            return False
            
        try:
            print("Loading Keras model...")
            self.model = tf.keras.models.load_model(self.model_path)
            print("Model loaded successfully!")
            print(f"Model summary:")
            self.model.summary()
            return True
            
        except Exception as e:
            print(f"Error loading model: {e}")
            return False
    
    def predict(self, data: Union[np.ndarray, pd.DataFrame]) -> np.ndarray:
        """
        Make predictions using the loaded model
        
        Args:
            data: Input data for prediction
            
        Returns:
            Model predictions
        """
        if self.model is None:
            raise ValueError("Model not loaded. Please load the model first.")
            
        if isinstance(data, pd.DataFrame):
            data = data.values
            
        predictions = self.model.predict(data)
        return predictions
    
    def get_model_info(self) -> dict:
        """
        Get information about the loaded model
        
        Returns:
            Dictionary with model information
        """
        if self.model is None:
            return {"status": "Model not loaded"}
            
        return {
            "model_id": self.model_id,
            "input_shape": self.model.input_shape,
            "output_shape": self.model.output_shape,
            "total_params": self.model.count_params(),
            "layers": len(self.model.layers)
        }

def main():
    """
    Example usage of the GenomicsModelLoader
    """
    print("=== Genomics Model Loader Demo ===")
    
    # Initialize the loader
    loader = GenomicsModelLoader()
    
    # Download the model
    model_path = loader.download_model()
    
    if model_path:
        # Load the model
        success = loader.load_model()
        
        if success:
            # Get model information
            info = loader.get_model_info()
            print(f"\nModel Information: {info}")
            
            # Example prediction (you would replace this with your actual genomics data)
            print("\nTo use this model, prepare your genomics data as a numpy array or pandas DataFrame")
            print("and call loader.predict(your_data)")
        else:
            print("Failed to load model")
    else:
        print("Failed to download model")

if __name__ == "__main__":
    main()