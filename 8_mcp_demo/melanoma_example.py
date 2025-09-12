from transformers import AutoImageProcessor, AutoModelForImageClassification
import torch
from PIL import Image
import requests

# Load the melanoma model
model_name = "UnipaPolitoUnimore/vit-large-patch32-384-melanoma"
print(f"Loading model: {model_name}")

image_processor = AutoImageProcessor.from_pretrained(model_name)
model = AutoModelForImageClassification.from_pretrained(model_name)

# Create a dummy image for demonstration since we don't have a real melanoma image
import numpy as np

try:
    print("Creating sample image for demonstration...")
    # Create a sample 384x384 RGB image (the model expects 384x384 input)
    dummy_image = np.random.randint(0, 255, (384, 384, 3), dtype=np.uint8)
    image = Image.fromarray(dummy_image)
    print(f"Sample image created: {image.size}")
    
    # Process the image
    inputs = image_processor(image, return_tensors="pt")
    
    # Make prediction
    print("Making prediction...")
    with torch.no_grad():
        logits = model(**inputs).logits
    
    # Get the predicted class
    predicted_class_id = logits.argmax(-1).item()
    
    # Check if model has label mapping
    if hasattr(model.config, 'id2label') and model.config.id2label:
        predicted_label = model.config.id2label[predicted_class_id]
        print(f"Prediction: {predicted_label}")
    else:
        print(f"Predicted class ID: {predicted_class_id}")
    
    # Show confidence scores
    probabilities = torch.softmax(logits, dim=-1)
    print(f"Confidence scores: {probabilities}")
    print(f"Max confidence: {probabilities.max().item():.4f}")
    
except Exception as e:
    print(f"Error: {e}")
    print("Make sure you have the required dependencies installed:")
    print("pip install transformers torch pillow requests")